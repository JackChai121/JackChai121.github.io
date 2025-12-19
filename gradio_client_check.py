from gradio_client import Client, handle_file

client = Client("JackHug121/CatDogDetector")
result = client.predict(
	img=handle_file('https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png'),
	api_name="/classify_image"
)
print(result)