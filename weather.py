#Author: Jacob Longfield Date: 7/20/2020
import requests 
import json

give_correct_value = False
is_zip = False
degree_sign = u"\N{DEGREE SIGN}"
continue_program = True


while continue_program == True:
	while give_correct_value == False:
		#Ask the user if they want to provide a zip code or a city name
		user_input = input('\nType in \'z\' for zip code or \'c\' for city name: ')

		#Try and parse user_input to an int for zipcode else is it a city name
		if user_input.lower() == 'z':
			try:
				#Obtain area information from user
				user_input = input('Enter in the zip code or the name of the city you wish to view the weather for: ')

				zip_code = int(user_input)
				is_zip = True
				give_correct_value = True
		
			except ValueError:
				print('The value you entered in is invalid')

		elif user_input.lower() == 'c':
			#Obtain area information from user
			user_input = input('Enter in the zip code or the name of the city you wish to view the weather for: ')

			city_name = user_input
			is_zip = False
			give_correct_value = True

		else:
			print('You did not select a correct input')


	url = 'https://api.openweathermap.org/data/2.5/weather?'
	api_key = 'f86a10565db60aa6a1c2994e6784e5bd'

	#Build the URL for the request
	if is_zip == True:
		url += (f'zip={zip_code}&appid={api_key}')
	else: 
		url += (f'q={city_name}&appid={api_key}')

	#Attempt to request the Json file from the URL
	try:
		r = requests.get(url)
		response = r.json()
	except :
		print('Connection Error. Try again Later')
		response = None
	else: 
		try:
			print(response['message'])
			response = None
		except KeyError:
			print("\nLink established\n")
			response = r.json()
	#Format the request's response 
	if response is not None:
		#Put all important data into a dictonary
		weather = {}
		weather['name']    = response['name']
		weather['forcast'] = response['weather'][0]['main']
		weather['type']    = response['weather'][0]['description']
		weather['temp']    = response['main']['temp']
		weather['high']    = response['main']['temp_max']
		weather['low']     = response['main']['temp_min']

		#Convert default of kelvin to F : (K - 273.15) * 9/5 + 32
		weather['temp'] = float(weather['temp'])
		weather['high'] = float(weather['high'])
		weather['low']  = float(weather['low'])

		weather['temp'] = round(((weather['temp'] - 273.15) * 9/5 + 32),2)
		weather['high'] = round(((weather['high'] - 273.15) * 9/5 + 32),2)
		weather['low']  = round(((weather['low'] - 273.15) * 9/5 + 32),2)

		#Print out data
		print(f"\n\n\nWeather for: {weather['name']}")
		print(f"Temp: {weather['temp']}{degree_sign}\t{weather['forcast']}, {weather['type']}")
		print(f"High: {weather['high']}{degree_sign}\tLow: {weather['low']}{degree_sign}")


	give_correct_value = False
	while give_correct_value == False:
		#Ask the user if they want to continue 
		user_input = input("\n\nWould you like to check another area? \'y\' for yes, \'n\' for no: ")

		#Check user_input
		if user_input.lower() == 'y':
			continue_program = True
			give_correct_value = True
		elif user_input.lower() == 'n':
			continue_program = False
			give_correct_value = True
		else:
			print('\nYou did not select a correct input')
	give_correct_value = False
