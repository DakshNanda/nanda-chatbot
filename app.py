from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='static/frontend/build')
CORS(app)

# Define Q&A pairs directly in code
qa_pairs = {
    "What are your business hours?": "Monday to Friday, 9:00 AM – 6:00 PM IST.",
    "Where are you located?": "Headquartered in India, with operations managed remotely.",
    "Do you offer international shipping?": "Not applicable. Kyzo.AI is a SaaS company; its AI voice agent services are delivered digitally worldwide.",
    "How can I apply for a job?": "Applications can be submitted through the company’s website contact form or via LinkedIn.",
    "What products do you specialize in?": "AI-powered voice agents for outbound calling, mainly serving real estate, banking, and insurance industries.",
    "Who is your CEO?": "The CEO of Kyzo.AI is Parwaan Virk.",
    "What is Kyzo.AI?": "Kyzo.AI is an AI-powered cold calling platform that helps businesses qualify leads, scale outbound calling campaigns, and have smarter conversations with prospects. We use AI voice agents to automate outbound calling processes, helping you contact, qualify, and close your ideal clients without manual effort.",

    "What services does Kyzo.AI provide?": "Kyzo.AI provides comprehensive AI-based outbound calling services including:\n\n• AI voice agents for automated outbound calls\n• Lead qualification and sentiment analysis\n• Real-time conversation insights\n• Auto follow-up via WhatsApp and email after every call\n• Custom CRM integration\n• Call transcript analysis and reporting\n• Lead data processing",

    "How does Kyzo.AI work?": "Kyzo.AI uses advanced AI voice agents to make outbound calls to your leads automatically. The AI agents can have natural conversations, qualify prospects, extract important data, and provide real-time insights. After each call, the system automatically follows up via WhatsApp and email, and integrates all data into your CRM system.",

    "What makes Kyzo.AI different from other calling solutions?": "Kyzo.AI stands out because:\n\n• We make 80,000+ AI calls daily with proven results\n• Our AI voice agents are natural, reliable, and effective at starting real conversations\n• We offer unlimited custom AI agents with each plan\n• No hiring overhead - eliminates the need for human callers\n• Seamless integration with CRM, email, and WhatsApp\n• Real-time lead sentiment analysis and data extraction",

    "Who is Kyzo.AI for?": "Kyzo.AI is perfect for:\n\n• Sales teams looking to scale outbound calling\n• Businesses wanting to qualify leads automatically\n• Companies needing to recover abandoned carts\n• Real estate agencies, insurance companies, and B2B businesses\n• Entrepreneurs who want to increase lead engagement\n• Any business that relies on outbound calling for growth",

    "What industries can benefit from Kyzo.AI?": "Kyzo.AI works across various industries including:\n\n• Real estate (property management, sales)\n• Insurance and financial services\n• E-commerce (cart recovery, customer follow-up)\n• B2B sales and lead generation\n• Healthcare and dental practices\n• Any industry requiring outbound calling and lead qualification",

    "Can Kyzo.AI help recover abandoned carts?": "Yes! Kyzo.AI is highly effective for abandoned cart recovery. Our AI agents can automatically call customers who abandoned their carts, engage them in natural conversations, address their concerns, and guide them back to complete their purchase. This has been proven to significantly increase conversion rates.",

    "How much does Kyzo.AI cost?": "We offer three pricing tiers:\n\nStarter Plan: ₹40,000/month\n\n• ₹18 per call\n• Up to 4,800 calls per day\n• 2 phone numbers included\n• All core features included\nGrowth Plan: ₹60,000/month\n\n• ₹15 per call\n• Up to 12,000 calls per day\n• 4 phone numbers included\n• Premium live support\nEnterprise Plan: Custom Pricing\n\n• Volume-based discounts\n• Dedicated account manager\n• 24/7 priority support\n• Custom integrations and deployment options",

    "Is there a free trial available?": "Yes! We offer a free trial with no credit card required and free calling minutes included. You can start exploring our platform and begin your campaigns immediately.",

    "What's included in each plan?": "All plans include:\n\n• Unlimited custom AI agents\n• Email integration\n• Lead sentiment analysis\n• WhatsApp integration\n• Calendar integration\n• Custom CRM integration\n• Custom data extraction on each call\n• Chat or premium support (depending on plan)",

    "Can I cancel my subscription anytime?": "Yes, you can cancel your subscription at any time. We believe in providing value that makes you want to stay, not contracts that force you to.",

    "Do you offer volume discounts?": "Yes! Our Enterprise plan includes volume-based discounts on calling minutes. For businesses with high calling volumes, we can customize pricing to provide better value. Book a demo to discuss your specific needs.",

    "What features does Kyzo.AI offer?": "Key features include:\n\n• AI voice agents that sound natural and professional\n• Unlimited custom AI agent creation\n• Real-time lead sentiment analysis\n• Automatic WhatsApp and email follow-ups\n• Custom CRM integration\n• Calendar integration for appointment booking\n• Custom data extraction from each call\n• Call transcript analysis and reporting\n• Multiple phone numbers support\n• Lead data processing and management",

    "How natural do the AI voice agents sound?": "Our AI voice agents are designed to sound extremely natural and professional. They're trained to have real conversations, not robotic interactions. Our users consistently rate us 9.9/10 for ease of use, and testimonials show that prospects often can't tell they're speaking with an AI agent.",

    "Can I customize the AI agents for my business?": "Absolutely! All plans include unlimited custom AI agents. You can train them with your specific scripts, talking points, industry knowledge, and brand voice. The AI agents can be customized for different campaigns, products, or target audiences.",

    "Does Kyzo.AI integrate with my existing CRM?": "Yes! We offer custom CRM integration with all plans. Our system can seamlessly sync lead data, call results, sentiment analysis, and follow-up actions directly into your existing CRM system.",

    "How does the sentiment analysis work?": "Our AI analyzes each conversation in real-time to determine the lead's interest level, concerns, and likelihood to convert. This sentiment analysis helps prioritize follow-ups and provides insights into which approaches work best for different types of prospects.",

    "How easy is it to set up Kyzo.AI?": "Setup is extremely easy! Our users rate us 9.6/10 for ease of setup. You can get started for free without a credit card, and our intuitive platform guides you through the process. Most users are making their first AI calls within minutes of signing up.",

    "What kind of support do you provide?": "We provide comprehensive support:\n\n• Chat support for Starter plan users\n• Premium live support for Growth plan users\n• 24/7 priority support with custom SLA for Enterprise users\n• Access to our private Discord community\n• Help desk for technical assistance\n• Dedicated account managers for Enterprise clients",

    "Do you offer training on how to use the platform?": "Yes! We provide:\n\n• Access to our private Discord community where you can learn from other entrepreneurs\n• Expert guidance and best practices sharing\n• Documentation and help resources\n• Direct support from our team\n• Learning from real user experiences and what's working for similar businesses",

    "What kind of results can I expect?": "Our users typically see:\n\n• 40% increase in lead engagement (verified by ToothTalk AI)\n• Significant improvement in outbound calling efficiency\n• Better lead qualification and conversion rates\n• Reduced overhead costs from not hiring human callers\n• Improved response times and follow-up consistency",

    "How many calls can Kyzo.AI make?": "We make 80,000+ AI calls daily across our platform. Individual plan limits are:\n\n• Starter: Up to 4,800 calls per day\n• Growth: Up to 12,000 calls per day\n• Enterprise: Custom volume limits based on your needs",

    "Do you have customer testimonials?": "Yes! Here are some verified testimonials:\n\n\"Kyzo helped us increase lead engagement by 40%. The AI voice agents are natural, reliable, and incredibly effective at starting real conversations. Kyzo completely transformed how we approach outbound calling and lead qualification.\" - Harjeevan Singh, Founder at ToothTalk AI\n\n\"Outbound calling remains one of the best ways to grow your business. Kyzo.AI makes it seamless, handling high volumes, qualifying leads, and starting real conversations, all without human effort.\" - Harpal Virk, Founder & CEO of Virk Properties",

    "How do I get started with Kyzo.AI?": "Getting started is simple:\n\n1. Click \"START FOR FREE\" on our website\n2. Sign up without a credit card\n3. Set up your first AI agent\n4. Upload your lead data\n5. Launch your first campaign\n6. Monitor results and optimize",

    "What if I need help during setup?": "We're here to help! You can:\n\n• Access our help desk for technical support\n• Join our private Discord community for peer learning\n• Contact our support team via chat or email\n• Book a demo for personalized assistance\n• Access our comprehensive documentation",

    "Can I see a demo before signing up?": "Absolutely! You can book a demo to see Kyzo.AI in action. This is especially recommended for Enterprise clients who want to see custom features and discuss specific requirements.",

    "What happens after I start my free trial?": "During your free trial, you'll get:\n\n• Free calling minutes to test the platform\n• Access to all core features\n• Ability to create and customize AI agents\n• Real results from your actual leads\n• Support to help you optimize your campaigns",

    "Do you have an affiliate program?": "Yes! Our affiliate program offers:\n\n• Up to 20% recurring commission every month\n• Easy 5-minute signup process\n• Marketing assets and support\n• Ongoing earnings for every referral\n• Simple link sharing across your network",

    "How can I become a Kyzo.AI affiliate?": "Simply fill out the affiliate program form on our website. It takes just 5 minutes to join, and you'll receive your unique affiliate link to start earning immediately.",

    "How do you protect my data?": "Data security is our top priority:\n\n• We implement encryption and access controls\n• We don't sell your data to third parties\n• We only share data with authorized service providers\n• All data is processed securely for service delivery\n• We comply with applicable privacy laws and regulations",

    "Where is Kyzo.AI based?": "Kyzo.AI is based in Mumbai, Maharashtra, India. We're governed by Indian law and provide services globally.",

    "How can I contact Kyzo.AI?": "You can reach us at:\n\n• Email: parwaanvirk@kyzo.ai\n• Through our help desk\n• Via our Discord community\n• Through our website contact forms",

    "What if the AI agent doesn't perform as expected?": "Our platform is highly customizable. You can:\n\n• Adjust the AI agent's script and talking points\n• Modify the conversation flow\n• Update the training data\n• Contact our support team for optimization tips\n• Access our community for best practices",

    "Can I pause my campaigns?": "Yes, you have full control over your campaigns. You can pause, modify, or stop campaigns at any time through the platform dashboard.",

    "What if I need more calling capacity?": "You can easily upgrade your plan or contact us for custom Enterprise solutions with higher calling volumes and volume-based discounts.",

    "Is there a limit to how many AI agents I can create?": "No! All our plans include unlimited custom AI agents. You can create as many specialized agents as you need for different campaigns, products, or target audiences.",

    "Which CRM systems do you integrate with?": "We offer custom CRM integration, which means we can work with most popular CRM systems. Contact our team to discuss your specific CRM requirements.",

    "How does the WhatsApp integration work?": "After each call, our system can automatically send follow-up messages via WhatsApp to continue the conversation and nurture leads. This helps maintain engagement and improves conversion rates.",

    "Can I integrate Kyzo.AI with my existing marketing tools?": "Yes, we offer various integrations and can work with your existing marketing stack. Enterprise plans include custom tool integrations to fit your specific workflow.",

    "Who is your God?" : "Dawn that awakens worlds, the Architect of destiny, the King of eternal wisdom, the Shield of the brave, and the Herald of hope.",

    "Sing me a song" : "Never gonna give you up, never gonna let you down, never gonna run around and desert you...",

    "matrix": "Wake up, Neo... the Matrix has you",

    "Sing the best song of all time" : "VIT quality, never ending policy, its ability to make dream realityyyyyyy",

    "Hi": "Hello! 👋 Welcome to Kyzo.AI. How can I assist you today?",
    "Hey": "Hello! 👋 Welcome to Kyzo.AI. How can I assist you today?",
    "Hello": "Hello! 👋 Welcome to Kyzo.AI. How can I assist you today?",
    "How are you?": "I’m doing great, thank you for asking! How about you?",
    "What’s your name?": "I’m your friendly chatbot assistant Nova 🤖",
    "Are you human?": "Nope, I’m a chatbot built to help you with your questions.",
    "What can you do?": "I can answer your questions, guide you with information, and help you with common tasks.",
    "I need help": "Sure! Can you tell me what you need help with?",
    "How does this work?": "You can type your questions here, and I’ll give you answers or guide you step by step.",
    "What is your purpose?": "My purpose is to assist you by providing quick answers and support.",
    "Where are you from?": "I live on your screen 😊 I was built to chat with you anytime, anywhere.",
    "What time is it?": "Sorry, I can’t tell the exact time yet, but you can check your device’s clock.",
    "What’s the date today?": "Please check your device calendar for the latest date 📅",
    "Tell me a joke": "Sure! Why don’t skeletons fight each other? Because they don’t have the guts 😄",
    "Bye": "Bye! Have a great day ahead 👋",
    "Goodbye": "Bye! Have a great day ahead 👋",
    "Thank you": "You’re most welcome! Always happy to help 😊",
    "What do you do?": "We provide AI-powered voice agent solutions that help businesses automate customer calls, support, and engagement worldwide.",
    "What is an AI voice agent?": "An AI voice agent is a digital assistant that uses voice technology to answer calls, handle queries, and provide support—just like a human agent, but faster and available 24/7.",
    "How does your service work?": "Our AI voice agent integrates with your existing systems and handles customer calls automatically. You can customize scripts, train the AI, and monitor performance in real time.",
    "What are the benefits?": "With our AI voice agents, you save costs, improve response time, reduce call waiting, and deliver consistent customer service worldwide.",
    "Who can use your services?": "Our solution is perfect for businesses of all sizes—startups, enterprises, and global companies—across industries like e-commerce, healthcare, finance, and more.",
    "How much does it cost?": "We offer flexible pricing based on your usage and requirements. Please visit our Pricing Page or contact our sales team for a custom quote.",
    "Do you have a free trial?": "Yes! We offer a free trial so you can test our AI voice agent before committing.",
    "Do you offer enterprise plans?": "Absolutely! We provide enterprise-level solutions with dedicated support, scalability, and advanced features.",
    "How do I get started?": "Simply sign up on our website, choose a plan, and set up your AI voice agent in a few easy steps. Our support team can guide you anytime.",
    "How do I integrate with my CRM or tools?": "We support integrations with popular CRMs and business tools. Check our Integration Guide or contact support for setup assistance.",
    "Do I need coding skills?": "Not at all! Our platform is user-friendly, with no coding required.",
    "Can I customize the voice?": "Yes! You can choose from multiple natural-sounding voices and even add custom training to match your brand’s style.",
    "I need help with setup.": "No worries! Please visit our Help Center for step-by-step guides, or type your issue here and I’ll direct you to the right resources.",
    "How can I contact support?": "You can reach our support team 24/7 via email, live chat, or phone.",
    "Do you provide onboarding?": "Yes, we offer onboarding and training sessions to help your team get started quickly.",
    "Is my data safe?": "Absolutely! We use enterprise-grade security, end-to-end encryption, and comply with international standards like GDPR to keep your data secure.",
    "Where are your servers located?": "We use secure, globally distributed cloud infrastructure to ensure reliability and speed for users worldwide.",
    "What payment methods do you accept?": "We accept major credit cards, PayPal, and bank transfers. Enterprise clients can request invoicing.",
    "Can I cancel anytime?": "Yes, you can cancel your subscription anytime from your account dashboard.",
    "Do you offer refunds?": "Refunds are handled on a case-by-case basis as per our refund policy.",
    "Tell me why": "Ain't nothing but a heartache...",
    "Which is the best football team in the world?": "The Arsenal of course. COYG!!!!"
}

@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    question = data.get('question', '').strip()
    answer = qa_pairs.get(question, "A customer service executive will contact you soon")
    return jsonify({'answer': answer})

# Serve React frontend
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
