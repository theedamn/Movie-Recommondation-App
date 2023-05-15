from movie import *
import PySimpleGUI as sg

# Define the layout of the GUI
layout = [
    [sg.Text("Enter your query:"), sg.InputText(key='-INPUT-')],
    [sg.Text("Number of results:"), sg.Combo(values=[5, 10, 15], default_value=5, key='-NUM_RESULTS-')],
    [sg.Text("Alogithms"), sg.Combo(values=['Cosine','PineCone','ANN'], default_value='Cosine', key='-FUNC-')],
    [sg.Button("Display"), sg.Button("Clear")],
    [sg.Text("Search Results:")],
    [sg.Output(size=(100, 40), key='-OUTPUT-')]
]

# Create the window
window = sg.Window("Movie Recommender App", layout)

# Event loop to process events and interact with the GUI
while True:
    event, values = window.read()

    # If the window is closed or "Clear" button is clicked, exit the loop
    if event == sg.WINDOW_CLOSED :
        break


    if event == "Clear":
        window['-OUTPUT-'].update("")
        #continue

    # Handle button events
    if event == "Display":
        
        nos=values['-NUM_RESULTS-']
        
        algo=values['-FUNC-']
        
        query = values['-INPUT-']
        if algo == 'Cosine':
            Output_Title,Output_Summary=similarity_search_Cos_Sim(query,nos)
        if algo == 'PineCone':
            Output_Title,Output_Summary=similarity_search_pinecone(query,nos)
        if algo == 'ANN':
            Output_Title,Output_Summary=similarity_search_ANN(query,nos)


        # Print the entered query in the output box
        # print(f"Entered Query: {Output}")
        for _ in range(len(Output_Title)):
            print("Title: {}".format(Output_Title[_]))
            print("-" * 50)  # Print a separator line
            print("Summary: {}".format(Output_Summary[_]))
            print()



# Close the window
window.close()
