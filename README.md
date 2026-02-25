# Paysafe AI Solution Case Study

## Problem understanding

#### What problem you are solving  
- Create an AI assistant prototype to help internal support agents quickly understand and respond to customer enquiries
- The assistant will:
  - analyse incoming messages
  - identify intent and key information
  - suggest actions
  - provide confidence indicators

#### What you deliberately did not solve
- I did not create an AI assistant that processes and responds to customer enquiries directly
- I did not design a user-friendly interface for support agents to interact with the AI assistant

## Design decisions

#### Why you chose your approach:
- Structured LLM Output
    - Using Pydantic models ensures consistent format for the AI assistant's output, making it easier for support agents to read and understand the analysis quickly
    - Detailed description fields reduce potential hallucinations by guiding the model to provide specific types of information

#### Model and tooling choices:  
- OpenAI offers a batch solution for requests, which I had considered using. Although, batch processing is more suited towards a very large number of requests with a longer latency, which isn't suitable for live customer support data. With the given scope of the prototype, this is not necessary but it might be worth looking into this further in the future.
- The model I used is OpenAI's GPT-5-nano, because it is a cheap but powerful model that is suitable for prototyping and the given scope of the project.

#### Trade-offs you made due to time constraints:  
- UI design and ease of use is not the focus of the prototype, so the interface is basic and functional rather than polished.
- The System Prompt and prompts in the Pydantic model can be refined further to improve the quality of the AI's output, but I focused on getting a working prototype within the time limit.
- The scope assumes data is anonymous, so the current solution will send the whole enquiry to the AI assistant. In the future, the enquiry will need to be stripped of all personal or sensitive information before being sent to the AI assistant.

## Corporate readiness

#### How this would work in a regulated environment:
- Prior to deployment, the AI assistant would be thoroughly tested on accuracy and bias to ensure it provides reliable and helpful suggestions.
- The AI assistant provides its opinion on escalation, but the support agent has the final decision on whether to escalate or not.

#### Data handling considerations:
- Enquiries must be anonymised before being sent to the AI assistant to ensure no personal information is exposed.
- Within the logging system, I would ensure that no personal or sensitive information is stored, and only the AI's analysis and suggestions are logged for review.
- The logging system would not store records permanently, and logs would be deleted after a short period to further protect data privacy.

#### Human-in-the-loop approach:
- The AI assistant is designed to only make recommendations to support agents, and will not have the ability to take actions directly. This means support agents have the final decision in all cases.
- The confidence scores provided by the AI assistant allow support agents to make informed decisions on whether to trust the AI's suggestions or not.
- The support agents will have the ability to provide feedback on the AI's suggestions, which can be used to further improve the model's performance over time.

## Next steps

#### What you would improve with more time:
- I would put more effort into the UI design, potentially opting for a simple web app, to make it more user-friendly for support agents.
- To improve accuracy and reduce hallucinations, I would integrate a RAG (Retrieval-Augmented Generation) approach, where the AI assistant can access a knowledge base of relevant information to support its analysis and suggestions.

#### How you would take this towards production at Paysafe:
- Depending on the number of enquiries the support agents receives, I would consider automating the processing of each enquiry using the AI assistant, which then can sort and send to the support agents for review and response. This would further reduce manual effort and improve efficiency as:  
    - The AI assistant can quickly analyse and categorise incoming messages
    - Support agents can review the AI-generated analysis to understand the context and intent of the enquiry allowing them to focus on crafting responses rather than sorting through messages
- To ensure the AI assistant works as intended and provides accurate and helpful suggestions, I would implement a logging system to track the AI's outputs. This would assist in identifying errors with the system for future review and improvement.
