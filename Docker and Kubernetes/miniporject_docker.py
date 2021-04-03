from flask import Flask
import json, requests, requests_cache,jsonify,tweepy
from flask_sqlalchemy import SQLAlchemy
from flask_restful import fields,abort,reqparse, Api, Resource, marshal_with

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:testdatabase@database-1.cdz011ps0tg4.us-east-1.rds.amazonaws.com:3306/miniproject'
db = SQLAlchemy(app)


class BookModel(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	ISBN_10 = db.Column(db.Integer, nullable = True)
	Language = db.Column(db.String(10), nullable = False)
	Title = db.Column(db.String(100), nullable = False)
	Subtitle = db.Column(db.String(100), nullable = True)
	Author = db.Column(db.String(100), nullable = False)
	Publisher = db.Column(db.String(100), nullable = False)
	Published_Date = db.Column(db.String(40), nullable = False)
	Page_Count = db.Column(db.Integer, nullable = True)
	Category = db.Column(db.String(40), nullable = False)
	Content_Version = db.Column(db.String(40), nullable = True)
	Sale_Country = db.Column(db.String(40), nullable = True)
	Description = db.Column(db.String(1000), nullable = True)
	Retail_Price = db.Column(db.String(40), nullable = True)
	List_Price = db.Column(db.String(40), nullable = True)

	def __repr__(self):
		return f"Book(ISBN_10={ISBN_10},Language={Language},Title={Title},Subtitle={Subtitle},Author={Author},Publisher={Publisher},Published_Date={Published_Date},Page_Count={Page_Count},Category={Category},Content_Version={Content_Version},Sale_Country={Sale_Country},Description={Description},Retail_Price={Retail_Price},List_Price={List_Price})"

#only uncomment on first run otherwise database would be overwritten
#db.create_all()


books_put_args = reqparse.RequestParser()
books_put_args.add_argument("ISBN_10", type= int, help="ISBN10 of the book")
books_put_args.add_argument("Language", type= str, help="Language of the book is required" , required = True)
books_put_args.add_argument("Title", type= str, help="Title of the book is required", required = True)
books_put_args.add_argument("Subtitle", type= str, help="Subtitle of the book")
books_put_args.add_argument("Author", type= str, help="Author of the book is required" , required = True) 
books_put_args.add_argument("Publisher", type= str, help="Publisher of the book is required" , required = True)
books_put_args.add_argument("Published_Date", type= str, help="Published Date of the book is required" , required = True)
books_put_args.add_argument("Page_Count", type= int, help="Page Count of the book is required" , required = True)
books_put_args.add_argument("Category", type= str, help="Category of the book is required" , required = True) 
books_put_args.add_argument("Content_Version", type= str, help="Content Version of the book")
books_put_args.add_argument("Sale_Country", type= str, help="Sale Country of the book")
books_put_args.add_argument("Description", type= str, help="Description of the book")
books_put_args.add_argument("Retail_Price", type= str, help="Retail Price of the book")
books_put_args.add_argument("List_Price", type= str, help="List Price of the book")

book_update_args = reqparse.RequestParser()
book_update_args.add_argument("ISBN_10", type= int, help="ISBN10 of the book")
book_update_args.add_argument("Language", type= str, help="Language of the book is required")
book_update_args.add_argument("Title", type= str, help="Title of the book is required")
book_update_args.add_argument("Subtitle", type= str, help="Subtitle of the book")
book_update_args.add_argument("Author", type= str, help="Author of the book is required") 
book_update_args.add_argument("Publisher", type= str, help="Publisher of the book")
book_update_args.add_argument("Published_Date", type= str, help="Published Date of the book")
book_update_args.add_argument("Page_Count", type= int, help="Page Count of the book")
book_update_args.add_argument("Category", type= str, help="Category of the book") 
book_update_args.add_argument("Content_Version", type= str, help="Content Version of the book")
book_update_args.add_argument("Sale_Country", type= str, help="Sale Country of the book")
book_update_args.add_argument("Description", type= str, help="Description of the book")
book_update_args.add_argument("Retail_Price", type= str, help="Retail Price of the book")
book_update_args.add_argument("List_Price", type= str, help="List Price of the book")

resource_fields = {
	'id': fields.Integer,
	'ISBN_10': fields.Integer,
	'Language': fields.String,
	'Title': fields.String,
	'Subtitle': fields.String,
	'Author': fields.String,
	'Publisher': fields.String,
	'Published_Date': fields.String,
	'Page_Count': fields.Integer,
	'Category': fields.String,
	'Content_Version': fields.String,
	'Sale_Country': fields.String,
	'Description': fields.String,
	'Retail_Price': fields.String,
	'List_Price': fields.String
}


class Book(Resource):
	@marshal_with(resource_fields)
	def get(self, book_ISBN13):
		result = BookModel.query.filter_by(id = book_ISBN13).first()
		if not result:
			abort(404, message= "Book does not exist in the system")
		return result

	@marshal_with(resource_fields)
	def put(self, book_ISBN13):
		args = books_put_args.parse_args()
		result = BookModel.query.filter_by(id = book_ISBN13).first()
		if result:
			abort(409, message= "Book already exists")

		book = BookModel(id= book_ISBN13, ISBN_10= args["ISBN_10"],Language=args["Language"],Title=args["Title"],Subtitle=args["Subtitle"],Author= args["Author"],Publisher=args["Publisher"],Published_Date=args["Published_Date"],Page_Count=args["Page_Count"],Category=args["Category"],Content_Version=args["Content_Version"],Sale_Country=args["Sale_Country"],Description=args["Description"],Retail_Price=args["Retail_Price"],List_Price=args["List_Price"])
		db.session.add(book)
		db.session.commit()
		return book, 201

	@marshal_with(resource_fields)
	def patch(self, book_ISBN13):
		args = book_update_args.parse_args()
		q2 = BookModel.query.filter_by(id = book_ISBN13).first()
		if not q2:
			abort(404, message = "Book which you are trying to update does not exist")

		if args['ISBN_10']:
			q2.ISBN_10 = args['ISBN_10']
		if args['Language']:
			q2.Language = args['Language']
		if args['Title']:
			q2.Title = args['Title']
		if args['Subtitle']:
			q2.Subtitle = args['Subtitle']
		if args['Author']:
			q2.Author = args['Author']
		if args['Publisher']:
			q2.Publisher = args['Publisher']
		if args['Published_Date']:
			q2.Published_Date = args['Published_Date']
		if args['Page_Count']:
			q2.Page_Count = args['Page_Count']
		if args['Category'] in args:
			q2.Category = args['Category']
		if args['Content_Version'] in args:
			q2.Content_Version = args['Content_Version']
		if args['Sale_Country'] in args:
			q2.Sale_Country = args['Sale_Country']
		if args['Description']:
			q2.Description = args['Description']
		if args['Retail_Price'] in args:
			q2.Retail_Price = args['Retail_Price']
		if args['List_Price'] in args:
			q2.List_Price = args['List_Price']

		db.session.commit()

		return q2, 200

	def delete(self, book_ISBN13):
		args = book_update_args.parse_args()
		q2 = BookModel.query.filter_by(id = book_ISBN13).first()
		if not q2:
			abort(404, message = "Book which you are trying to delete does not exist")
		q3 = BookModel.query.filter_by(id = book_ISBN13).delete()

		db.session.commit()
		return '', 204

api.add_resource(Book, "/book/<int:book_ISBN13>")


URL = 'https://www.googleapis.com/books/v1/volumes'
JSON_LIST = 'readinglist.json'
def search(query, max):
    queryKey = 'q' # variable for 'q'
    
    query = "+".join(query.split())
    query_params = {
        queryKey: query,
        'maxResults': max
    }
    ki=0
    response = requests.get(URL, params = query_params)
    result = []
    for response in response.json()['items']: # loop through Books List
            res_dic = {"ID":"","ISBN_13": "","ISBN_10":"","Language":"","Title":"","Subtitle":"","Category":"","Author":"","Publishing company": "", "Published Date": "", "Content Version" : "","Description": "","pageCount":"","Sale Country":"","Is Book Available for Purchase on Google Books?":"","List Price":"","Retail Price":"","Preview Link":""}
            if 'id' in response:
                res_dic["ID"] = response['id']
            else:
                res_dic["ID"] = "N/A"
            if 'title' in response['volumeInfo']:
                res_dic["Title"] = response['volumeInfo']['title']
            else:
                res_dic["Title"] = "N/A"
            if 'authors' in response['volumeInfo']:
                res_dic["Author"] = response['volumeInfo']['authors'][0]
            else:
                res_dic["Author"] = "N/A"
            if 'publisher' in response['volumeInfo']:
                res_dic["Publishing company"] = response['volumeInfo']['publisher']
            else:
                res_dic["Publishing company"] = "N/A"
            if 'publishedDate' in response['volumeInfo']:
                res_dic["Published Date"] =  response['volumeInfo']['publishedDate']
            else: 
                res_dic["Published Date"] = "N/A"
            if 'description' in response['volumeInfo']:
                res_dic["Description"] =  response['volumeInfo']['description']
            else: 
                res_dic["Description"] = "N/A"
                
            if 'description' in response['volumeInfo']:
                res_dic["Description"] =  response['volumeInfo']['description']
            else: 
                res_dic["Description"] = "N/A"    
            if 'subtitle' in response['volumeInfo']:
                res_dic["Subtitle"] = response['volumeInfo']['subtitle']
            else:
                res_dic["Subtitle"] = "N/A"
            if 'industryIdentifiers' in response['volumeInfo']:
                res_dic["ISBN_13"] = response['volumeInfo']['industryIdentifiers'][0]['identifier']
            else:
                res_dic["ISBN_13"] = "N/A"
            try:
                if 'industryIdentifiers' in response['volumeInfo']:
                    res_dic["ISBN_10"] = response['volumeInfo']['industryIdentifiers'][1]['identifier']
            except:
                res_dic["ISBN_10"] = "N/A"
                
            if 'pageCount' in response['volumeInfo']:
                res_dic["Page Count"] =  response['volumeInfo']['pageCount']
            else: 
                res_dic["Page Count"] = "N/A"  
            if 'categories' in response['volumeInfo']:
                res_dic["Category"] = response['volumeInfo']['categories'][0]
            else:
                res_dic["Category"] = "N/A"
                
            if 'contentVersion' in response['volumeInfo']:
                res_dic["Content Version"] = response['volumeInfo']['contentVersion']
            else:
                res_dic["Content Version"] = "N/A"
                
            if 'language' in response['volumeInfo']:
                res_dic["Language"] = response['volumeInfo']['language']
            else:
                res_dic["Language"] = "N/A"
                
            if 'previewLink' in response['volumeInfo']:
                res_dic["Preview Link"] = response['volumeInfo']['previewLink']
            else:
                res_dic["Preview Link"] = "N/A"
                
            try:
                    res_dic["Sale Country"] = response['saleInfo']['country']
            except:
                    res_dic["Sale Country"] = "N/A"
            try:
                    res_dic["Is Book Available for Purchase on Google Books?"] = response['saleInfo']['saleability']
            except:
                    res_dic["Is Book Available for Purchase on Google Books?"] = "Not known"
                    
            try:
                    res_dic["Retail Price"] = str(response['saleInfo']['retailPrice']['amount']) +" "+ str(response['saleInfo']['retailPrice']['currencyCode'])
            except:
                    res_dic["Retail Price"] = "N/A"
                    
            try:
                    res_dic["List Price"] = str(response['saleInfo']['listPrice']['amount']) +" "+ str(response['saleInfo']['listPrice']['currencyCode'])
            except:
                    res_dic["List Price"] = "N/A"
          
            result.append(res_dic)
            ki = ki +1
            result.append("==============================================================================END OF RESULT NUMBER %s=========================================================================================================="%(ki))
    return result
requests_cache.install_cache('googlebooks_cache', backend='sqlite', expire_after=36000)

@app.route('/googlebooks/<string:qq>')
def googlebooks(qq):

	results = search(qq, 40)
	resultq = json.dumps(results)
	return resultq


def TwitterSearch(q, no):
    # authenticating
    consumerKey = "ROe3u1f8pnvyrxWAZ347Z9YSb"
    consumerSecret = "RCYI8gA1So1mjkyNl8SU94r7P7ojQXXLwfifbzG3NEqRgrBXLO"
    accessToken = '527269368-zH9Vki5ZlethdSrrRO0GznBbCC15PIPHXztoCfq3'
    accessTokenSecret = 'IFkFmFSw2rfDgu5xDyw1xgJYjWt5HLE5rzEXb8p7gNJ3x'
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    api.retweet
    resulttwitter = []
    
    tweets = tweepy.Cursor(api.search, q=f"{q} -filter:retweets"  , lang = "en").items(no)
    count = 0

    for tweet in tweets:
    	resulttwitter.append(tweet.text)
    	resulttwitter.append("==============================================================================END OF TWEET %s=========================================================================================================="%(count))
    	count += 1
    return resulttwitter

@app.route('/twitter/<string:tt>')
def twitterapi(tt):
	new_results = TwitterSearch(tt , 100)
	return json.dumps(new_results)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
