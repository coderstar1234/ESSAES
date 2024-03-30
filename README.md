# Student Attendance and Performance Improvement System (ESSAES)

## Objective
The objective of this project is to create a system that merges IoT technology with personalized mentorship to improve student attendance and academic performance. The system aims to provide educational resources to support student learning and development while implementing strategies to effectively address challenges in attendance and academic performance.

## Approach
We have developed a prototype system that utilizes IoT devices for attendance tracking, a web-based platform for performance monitoring, and a mobile application for mentorship and support services.

### Implementation:
- **Prototype Development:** Develop a prototype using IoT devices for attendance tracking, a web-based platform for performance monitoring, and a mobile application for mentorship and support services.
- **Refinement:** Gather feedback from stakeholders to refine the system and address any issues or concerns.
- **Testing:** Conduct thorough testing to ensure the effectiveness and usability of the system.
- **Deployment:** Roll out the finalized version of the system across multiple educational institutions, continuously monitoring and improving its performance.
  
## Use Case Diagram
The system automatically tracks students' attendance and performance data, identifies at-risk students, provides personalized mentorship and support, and helps students improve their performance.

## Future Scope for Business
We aim to integrate additional features such as career counseling, skill development programs, and alumni networking to provide holistic support to students. The system is scalable and can be expanded to cater to various educational institutions globally through partnerships and collaborations.

## Project Mission
Our mission is to empower learners to master IoT technology through accessible and engaging educational resources.

## Features
- Interactive IoT tutorials covering various concepts and applications.
- Engaging quizzes to assess understanding and knowledge retention.
- Video lectures by industry experts and educators.
- Downloadable lecture notes and supplementary materials.
- Hands-on projects and experiments to apply learning in real-world scenarios.
- Chatbot for interactive assistance.

## Benefits
- Self-paced learning for individuals interested in IoT technology.
- Comprehensive resources suitable for beginners to advanced learners.
- Practical projects to enhance skills and understanding.
- Community forum for collaboration and discussion.

## Technology Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask
- **Database:** MongoDB
- **IoT Integration:** Raspberry Pi, Arduino, Sensors

## Contributors
- Himanshu Vashistha

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

# System Architecture Diagram
This diagram illustrates the components of your system: IoT devices for attendance tracking, a web-based platform for performance monitoring, and a mobile application for mentorship and support. The system interacts with a MongoDB database to store data.

![System Architecture Diagram](system_architecture_diagram.png)

## Installation
### Step 1: Install Flask and MongoDB
Ensure you have Flask installed using the command:
```bash
pip install Flask
Install MongoDB as your database. Refer to the MongoDB documentation for installation instructions based on your operating system.

Step 2: Project Structure
Create a directory structure as follows:

project_folder/
│
├── app.py
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── chatbot.html
│   ├── dashboard.html
│   ├── layout.html
│   └── technology_stack.html
│
├── static/
│   ├── css/
│   │   ├── style.css
│   │   └── chatbot.css
│   ├── js/
│   │   ├── script.js
│   │   └── chatbot.js
│   └── images/
│       ├── technology_stack_image.jpg
│       └── website_image.jpg
│
├── chatbot/
│   ├── intents.json
│   ├── train_chatbot.py
│   └── chatbot_model.pkl
│
└── LICENSE

