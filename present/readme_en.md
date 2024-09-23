# 1. Discord AI Bot
In this project, I used the Discord API to create a chatbot and connected it with multiple pre-trained models to achieve different task processing. When the user does not use commands, it will be handled by the `llama 3.1 70B` model, which has two tools, `get_time` and `RAG`, and users can use three commands:

`!transcribe`: Use the command to upload an `mp3` file to Discord, which will extract the lyrics from the music and display them on the UI.

`!readpdf`: Use the command to upload a `pdf` file to Discord, which will process the user's PDF into structured data stored on the server and provide the LLM's `RAG` tool for querying.

`!helper`: Print out all available commands and function explanations.

![discord aibot](discord_bot.png)
## Results
![discord bot preview](image.png)
![discord bot preview](image-1.png)

# 2. VST Presets Generator (in progress: data collection)
This project is currently under construction, with the main goal of training an NN model to provide a convenient UI for music producers to design sounds. The method is to upload an `mp3` file to the application, process it, and output a VST (Virtual Instrument Technology) plugin parameter file, which can be read by the plugin and produce a sound similar to the original `mp3` file.
![vst presets generator workflow](ai_vst_presets_generator.png)
## Project example
[![exist app example](image-3.png)](https://youtu.be/wE6-RZyjgnQ?si=gaV0-UR_K7ixG79T)

# 3. Federated MMoE
This is the main topic of my master's thesis research, aiming to develop a recommendation system that maximizes cache space utilization while considering user security and privacy issues. In this research, we use Federated learning to solve user security and privacy issues and accurately predict the probability of each user accessing movies through the MMoE model architecture. The process is:
1. Local Training: Each local server trains the model locally.
2. Central Averaging: After training the local model for several rounds, the model parameters are uploaded to the central server, where the central server averages the received model parameters and broadcasts them to each local model.
3. Local Re-training: After receiving the averaged parameters, the local model replaces the red block in the diagram with the averaged model parameters, keeping the other parts unchanged, and then continues to train the model, repeating steps 2 and 3 until convergence.

![Federated MMoE Diagram](fed_mmoe.png)
