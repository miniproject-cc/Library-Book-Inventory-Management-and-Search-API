import requests

# The BASE URL to be used

print("Press Enter to try adding some books")
input()

BASE = "http://127.0.0.1:5000/"

data = [{"ISBN_10":1234567899,"Language":"en","Title": "Machine Learning: The New Way","Subtitle": "Learn Machine Learning with Real Projects", "Author":"Joe Smith","Publisher": "Learning Media", "Published_Date": "22nd June 2019","Page_Count":322, "Category": "Computing", "Content_Version": "v1", "Sale_Country" : "GB","Description": "The Best Machine Learning Book in market", "Retail_Price" : "21 GBP", "List_Price" : "24.4 GBP"},
		{"ISBN_10":1234567829,"Language":"ar","Title": "Neural Networks: The New Way","Subtitle": "Learn Neural Networks with Real Projects", "Author": "Larry Smith","Publisher": "Learning Books", "Published_Date": "22nd May 2019","Page_Count":352, "Category": "AI", "Content_Version": "v1.1", "Sale_Country" : "AR","Description": "The Best Artifical Intelligence Book in market", "Retail_Price" : "22 GBP", "List_Price" : "24 GBP"},
		{"ISBN_10":1234567859,"Language":"fr","Title": "Artifical Intelligence: The New Way","Subtitle": "Learn Artifical Intelligence with Real Projects", "Author": "Kieth Smith", "Publisher": "Unique Media", "Published_Date": "22nd July 2019","Page_Count":342, "Category": "Computing", "Content_Version": "v3-new", "Sale_Country" : "FR","Description": "The Best Neural Networks Book in market", "Retail_Price" : "24 GBP", "List_Price" : "30 GBP"}]

# Add sone books using Put
for i in range(len(data)):
	response = requests.put(BASE + "book/" + str(1949191919119+(10*(i))), data[i])
	print(response.json())

print("-------------------------")
print("-------------------------")
print("Press Enter to try adding some books with missing data")
input()

# Add some books with required data missing

data1 = [{"ISBN_10":1234567899,"Title": "Machine Learning: The New Way","Subtitle": "Learn Machine Learning with Real Projects", "Author":"Joe Smith","Publisher": "Learning Media", "Published_Date": "22nd June 2019","Page_Count":322, "Category": "Computing", "Content_Version": "v1", "Sale_Country" : "GB","Description": "The Best Machine Learning Book in market", "Retail_Price" : "21 GBP", "List_Price" : "24.4 GBP"},
		{"ISBN_10":1234567829,"Language":"ar","Subtitle": "Learn Neural Networks with Real Projects", "Author": "Larry Smith","Publisher": "Learning Books", "Published_Date": "22nd May 2019","Page_Count":352, "Category": "AI", "Content_Version": "v1.1", "Sale_Country" : "AR","Description": "The Best Artifical Intelligence Book in market", "Retail_Price" : "22 GBP", "List_Price" : "24 GBP"},
		{"ISBN_10":1234567859,"Language":"fr","Title": "Artifical Intelligence: The New Way","Subtitle": "Learn Artifical Intelligence with Real Projects", "Publisher": "Unique Media", "Published_Date": "22nd July 2019","Page_Count":342, "Category": "Computing", "Content_Version": "v3-new", "Sale_Country" : "FR","Description": "The Best Neural Networks Book in market", "Retail_Price" : "24 GBP", "List_Price" : "30 GBP"}]


for i in range(len(data1)):
	response = requests.put(BASE + "book/" + str(1949291919119+(10*(i))), data1[i])
	print(response.json())

print("-------------------------")
print("-------------------------")
print("Press Enter to try retrieve book with ISBN_13: 1949191919119")
input()
response = requests.get(BASE + "book/1949191919119")
print(response.json())

print("-------------------------")
print("-------------------------")
print("Press Enter to try update book with ISBN_13: 1949191919129 with title 'Update Worked':")
input()
response = requests.patch(BASE + "book/1949191919129", {"Title" : "Update worked"})
print(response.json())

print("-------------------------")
print("-------------------------")
print("Press Enter to delete book with ISBN_13: 1949191919139:")
input()
response = requests.delete(BASE + "book/1949191919139")
print(response)
