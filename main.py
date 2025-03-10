import requests
def getResponse(prompt):
    # Define the API endpoint URL
    api_key = "AIzaSyBTDdskG_nHYAthpFjcjI1j4JweH_NAbTo"  # Replace with your actual API key
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
    data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }
    headers = {'Content-Type': 'application/json'}
    try:
        # Make a POST request to the API endpoint using requests.post()
        response = requests.post(url, json=data, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            res = response.json()
            return res
        else:
            print('Error:', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Error:', str(e))
        return None
    


prompt = input("Please Enter your prompt:")
a = getResponse(prompt)
file = open("Output.md", "w")
print(a['candidates'][0]['content']['parts'][0]['text'],file=file)