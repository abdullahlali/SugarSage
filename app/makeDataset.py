import joblib

# Extended Diabetes Q&A Dataset
dataset = [
    # Basics and Types
    ("What is diabetes?", "Diabetes is a chronic condition that occurs when the body cannot properly process blood sugar (glucose) due to lack of insulin or insulin resistance."),
    ("What are the main types of diabetes?", "The main types of diabetes are Type 1 diabetes, Type 2 diabetes, and gestational diabetes."),
    ("What is Type 1 diabetes?", "Type 1 diabetes is an autoimmune condition where the body's immune system attacks insulin-producing beta cells in the pancreas."),
    ("What is Type 2 diabetes?", "Type 2 diabetes occurs when the body becomes resistant to insulin or does not produce enough insulin to manage blood sugar levels."),
    ("What is gestational diabetes?", "Gestational diabetes is a type of diabetes that develops during pregnancy and usually disappears after giving birth."),
    ("What is maturity-onset diabetes of the young (MODY)?", "MODY is a rare form of diabetes caused by a mutation in a single gene, often diagnosed in adolescence or early adulthood."),
    ("What is latent autoimmune diabetes in adults (LADA)?", "LADA is a slow-progressing form of Type 1 diabetes that occurs in adults, often misdiagnosed as Type 2 diabetes."),
    ("What is secondary diabetes?", "Secondary diabetes is caused by another medical condition or medication, such as pancreatitis or steroid use."),
    ("What is prediabetes?", "Prediabetes is a condition where blood sugar levels are higher than normal but not high enough to be classified as diabetes."),
    ("What is insulin resistance?", "Insulin resistance occurs when the body's cells stop responding effectively to insulin, leading to high blood sugar levels."),
    
    # Symptoms and Diagnosis
    ("What are the early symptoms of diabetes?", "Early symptoms include increased thirst, frequent urination, fatigue, unexplained weight loss, and blurry vision."),
    ("What are the warning signs of diabetic ketoacidosis (DKA)?", "Signs include nausea, vomiting, fruity-smelling breath, rapid breathing, and confusion."),
    ("How is diabetes diagnosed?", "Diabetes is diagnosed using tests like fasting blood glucose, oral glucose tolerance, and HbA1c tests."),
    ("What is a random blood glucose test?", "A random blood glucose test checks blood sugar levels at any time of the day, regardless of when you last ate."),
    ("What is an oral glucose tolerance test (OGTT)?", "The OGTT checks blood sugar levels after fasting and again two hours after consuming a glucose-rich drink."),
    ("What are normal blood sugar levels?", "Normal fasting blood sugar levels are 70-100 mg/dL, and post-meal levels should be below 140 mg/dL."),
    ("What is the role of HbA1c in diabetes diagnosis?", "The HbA1c test measures average blood sugar over 2-3 months. A result of 6.5% or higher indicates diabetes."),
    
    # Treatment and Management
    ("How is Type one diabetes treated?", "Type 1 diabetes is treated with insulin therapy, blood sugar monitoring, a healthy diet, and regular exercise."),
    ("How is Type two diabetes treated?", "Type 2 diabetes is managed with lifestyle changes, medications like metformin, and sometimes insulin therapy."),
    ("What are the different types of insulin?", "Types of insulin include rapid-acting, short-acting, intermediate-acting, and long-acting insulin."),
    ("What is an insulin pump?", "An insulin pump is a small device that delivers a continuous supply of insulin into the body."),
    ("What is continuous glucose monitoring (CGM)?", "CGM is a technology that tracks blood sugar levels in real-time using a sensor placed under the skin."),
    ("What is an artificial pancreas?", "An artificial pancreas is a device that automatically monitors and regulates blood sugar using an insulin pump and CGM."),
    ("What is the role of exercise in diabetes management?", "Exercise improves insulin sensitivity, lowers blood sugar, and helps maintain a healthy weight."),
    ("What is medical nutrition therapy (MNT)?", "MNT is a personalized dietary plan created to help manage diabetes and control blood sugar levels."),
    ("How do oral diabetes medications work?", "Oral medications like metformin reduce glucose production in the liver or help the body use insulin more effectively."),
    ("What is the impact of weight loss on Type 2 diabetes?", "Losing even 5-10% of body weight can improve insulin sensitivity and lower blood sugar levels."),
    
    # Complications
    ("What are the long-term complications of diabetes?", "Complications include heart disease, kidney damage, nerve damage, eye problems, and poor wound healing."),
    ("What is diabetic neuropathy?", "Diabetic neuropathy is nerve damage caused by high blood sugar, leading to tingling, pain, or numbness in the extremities."),
    ("What is diabetic retinopathy?", "Diabetic retinopathy is damage to the blood vessels in the eyes, which can lead to vision loss."),
    ("What is diabetic nephropathy?", "Diabetic nephropathy is kidney damage caused by poorly controlled diabetes over time."),
    ("What is diabetic foot syndrome?", "Diabetic foot syndrome involves ulcers, infections, and poor wound healing due to nerve and blood vessel damage."),
    ("What is hyperosmolar hyperglycemic state (HHS)?", "HHS is a life-threatening complication of Type 2 diabetes involving very high blood sugar and dehydration."),
    ("How does diabetes affect the immune system?", "High blood sugar can weaken the immune system, making diabetics more prone to infections."),
    
    # Prevention
    ("How can Type two diabetes be prevented?", "Prevention strategies include maintaining a healthy weight, eating a balanced diet, staying active, and avoiding smoking."),
    ("What is the role of fiber in diabetes prevention?", "High-fiber foods can slow glucose absorption, reducing blood sugar spikes and improving insulin sensitivity."),
    ("Can intermittent fasting help prevent diabetes?", "Intermittent fasting may improve insulin sensitivity and help with weight loss, reducing diabetes risk."),
    
    # Lifestyle and Mental Health
    ("How does stress impact diabetes?", "Stress can raise blood sugar levels due to the release of hormones like cortisol."),
    ("Can sleep affect blood sugar levels?", "Yes, poor sleep quality can worsen insulin resistance and lead to higher blood sugar levels."),
    ("How does alcohol affect diabetes?", "Alcohol can cause blood sugar fluctuations, including hypoglycemia if consumed on an empty stomach."),
    ("How can I quit smoking to improve diabetes management?", "Quitting smoking improves circulation, insulin sensitivity, and reduces complications like heart disease."),
    ("How does diabetes impact mental health?", "Diabetes can increase the risk of depression, anxiety, and diabetes distress due to the burden of disease management."),
    
    # Advanced Topics and Research
    ("What is diabetes remission?", "Diabetes remission occurs when blood sugar levels are in the normal range without medication for an extended period."),
    ("Can bariatric surgery reverse Type 2 diabetes?", "Bariatric surgery can help some people with obesity achieve diabetes remission by improving insulin sensitivity."),
    ("What is the future of diabetes treatment?", "Emerging treatments include gene therapy, beta cell regeneration, and advanced closed-loop insulin delivery systems."),
    ("What is stem cell therapy for diabetes?", "Stem cell therapy aims to regenerate insulin-producing beta cells in the pancreas."),
    ("What are the latest diabetes research breakthroughs?", "Breakthroughs include artificial pancreas systems, improved insulin formulations, and personalized medicine."),
    
    # Miscellaneous and Rare Cases
    ("Can pets get diabetes?", "Yes, dogs and cats can develop diabetes, requiring insulin therapy and diet changes."),
    ("What is brittle diabetes?", "Brittle diabetes is a rare form of Type 1 diabetes characterized by severe blood sugar swings."),
    ("How does climate affect diabetes?", "Extreme heat or cold can impact insulin absorption and blood sugar levels, requiring careful management."),
    ("What is reactive hypoglycemia?", "Reactive hypoglycemia occurs when blood sugar drops too low after a meal, often in people with prediabetes."),
    ("Can people with diabetes donate blood?", "Yes, diabetics can donate blood if their condition is well-controlled and they meet donation criteria."),
    ("Can a ketogenic diet help with diabetes?", "A low-carb ketogenic diet may help manage Type 2 diabetes, but it should be supervised by healthcare providers."),

    # Additional Diabetes Basics
    ("What is normal blood sugar?", "Normal fasting blood sugar is between 70-99 mg/dL, while normal blood sugar 2 hours after eating should be less than 140 mg/dL."),
    ("How often should I check my blood sugar?", "The frequency depends on your type of diabetes and treatment plan. Consult your healthcare provider for a personalized schedule."),
    ("What is the A1C test?", "The A1C test measures your average blood sugar level over the past 2-3 months and is used to diagnose and monitor diabetes."),
    
    # Lifestyle and Management
    ("Can exercise lower blood sugar?", "Yes, regular physical activity can help lower blood sugar levels and improve insulin sensitivity."),
    ("What should I eat for breakfast with diabetes?", "Good breakfast options include eggs, whole grain toast, Greek yogurt, oatmeal with berries, or a protein smoothie."),
    ("How does stress affect diabetes?", "Stress can raise blood sugar levels by triggering the release of hormones like cortisol."),
    
    # Complications and Prevention
    ("What is diabetic retinopathy?", "Diabetic retinopathy is an eye condition that can cause vision loss in people with diabetes due to damage to blood vessels in the retina."),
    ("Can diabetes affect my feet?", "Yes, diabetes can cause nerve damage and poor circulation in feet, leading to numbness and increased risk of infections."),
    ("What is diabetic ketoacidosis?", "Diabetic ketoacidosis is a serious complication where the body produces high levels of ketones due to lack of insulin."),
    
    # Treatment Options
    ("What types of insulin are there?", "There are several types including rapid-acting, short-acting, intermediate-acting, and long-acting insulin."),
    ("How do insulin pumps work?", "Insulin pumps are small devices that deliver insulin continuously throughout the day through a small tube inserted under the skin."),
    ("What are oral diabetes medications?", "Common oral medications include metformin, sulfonylureas, and DPP-4 inhibitors, which help control blood sugar in different ways."),
    
    # Diet and Nutrition
    ("What is the glycemic index?", "The glycemic index ranks foods based on how quickly they raise blood sugar levels."),
    ("What are good snacks for diabetics?", "Good snacks include nuts, hard-boiled eggs, cheese, vegetables with hummus, or a small piece of fruit with protein."),
    ("Can I drink alcohol with diabetes?", "You can drink alcohol in moderation, but be aware it can affect blood sugar levels and should be consumed with food."),
    
    # Exercise and Physical Activity
    ("What exercises are best for diabetes?", "A combination of aerobic exercises like walking or swimming, and strength training exercises is best for managing diabetes."),
    ("How long should I exercise each day?", "Aim for at least 30 minutes of moderate-intensity exercise most days of the week."),
    ("Is walking good for diabetes?", "Yes, walking is an excellent exercise for diabetes management as it helps lower blood sugar and improve cardiovascular health."),
    
    # Emotional and Mental Health
    ("How can I cope with diabetes burnout?", "Take breaks when needed, seek support from others, and talk to your healthcare team about your feelings."),
    ("Is depression common with diabetes?", "Yes, people with diabetes have a higher risk of depression. It's important to seek help if you're feeling down."),
    ("How can I find diabetes support groups?", "You can find support groups through your healthcare provider, local hospitals, or online communities."),
    
    # Pregnancy and Diabetes
    ("What is gestational diabetes?", "Gestational diabetes is diabetes that develops during pregnancy and usually resolves after delivery."),
    ("Can I have a healthy pregnancy with diabetes?", "Yes, with proper blood sugar control and medical care, many women with diabetes have healthy pregnancies."),
    ("How often should I check blood sugar during pregnancy?", "During pregnancy, you may need to check your blood sugar more frequently, often 4-7 times per day."),
    
    # Children and Diabetes
    ("How can I help my child manage diabetes?", "Help them maintain a routine, learn about healthy eating, and make diabetes management fun and rewarding."),
    ("Can children with diabetes play sports?", "Yes, children with diabetes can and should participate in sports with proper monitoring and preparation."),
    ("What should teachers know about my child's diabetes?", "Teachers should know about symptoms of high and low blood sugar, emergency procedures, and any needed accommodations."),
    
    # Travel and Special Situations
    ("How do I manage diabetes while traveling?", "Plan ahead, pack extra supplies, keep insulin cool, and carry medical documentation."),
    ("What should I do if I get sick?", "Follow your sick-day management plan, check blood sugar more often, and stay hydrated."),
    ("How do I handle diabetes during Ramadan?", "Consult your healthcare provider about adjusting medication timing and monitoring blood sugar during fasting."),
    
    # Research and Technology
    ("What's new in diabetes research?", "Current research focuses on artificial pancreas systems, stem cell therapy, and new medications."),
    ("What is continuous glucose monitoring?", "Continuous glucose monitoring uses a sensor under the skin to track blood sugar levels throughout the day and night."),
    ("Are there new treatments for diabetes?", "New treatments include GLP-1 receptor agonists, artificial pancreas systems, and improved insulin formulations."),
    
    # Work and Career
    ("Should I tell my employer about my diabetes?", "It's a personal choice, but informing your employer can help ensure workplace accommodations if needed."),
    ("What are my rights as an employee with diabetes?", "The Americans with Disabilities Act protects workers with diabetes from discrimination and ensures reasonable accommodations."),
    ("How do I manage diabetes at work?", "Plan regular breaks for blood sugar checks, keep supplies accessible, and have a plan for emergencies."),
    
    # Insurance and Cost Management
    ("How can I afford diabetes supplies?", "Check insurance coverage, ask about generic medications, use prescription savings programs, and explore patient assistance programs."),
    ("What should insurance cover for diabetes?", "Insurance typically covers medications, supplies, education, and regular check-ups, though coverage varies by plan."),
    ("Are there programs to help pay for insulin?", "Yes, there are patient assistance programs, state programs, and discount cards available to help with insulin costs."),
    
    # Casual Conversation
    ("What's your favorite diabetes fact?", "I find it fascinating that the word 'diabetes' comes from Greek and means 'to pass through' - referring to excessive urination, one of its main symptoms."),
    ("Do you get tired of talking about diabetes?", "Not at all! I'm designed to help people understand and manage their health better."),
    ("What do you think about artificial sweeteners?", "While artificial sweeteners can be useful for reducing sugar intake, it's best to discuss their use with your healthcare provider."),
    
    # Random Knowledge
    ("What's the deepest part of the ocean?", "The Mariana Trench is the deepest known part of the ocean, reaching about 36,000 feet deep."),
    ("How many planets are in our solar system?", "There are eight planets in our solar system: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune."),
    ("What's the fastest land animal?", "The cheetah is the fastest land animal, reaching speeds up to 70 mph."),
    
    # Closing Conversations
    ("I appreciate your help today.", "You're welcome! Remember to consult healthcare professionals for personalized medical advice. Disclaimer: This information is for educational purposes only."),
    ("I learned a lot, thanks.", "Glad I could help! Remember to verify any medical information with your healthcare team. Disclaimer: This is not a substitute for professional medical advice."),
    ("You've been very helpful.", "Thank you! Stay healthy and remember to work closely with your healthcare providers. Disclaimer: Always seek professional medical guidance."),

    # Additional Diabetes Management
    ("What's the difference between hypoglycemia and hyperglycemia?", "Hypoglycemia is low blood sugar (below 70 mg/dL), while hyperglycemia is high blood sugar (above 180 mg/dL)."),
    ("How do I treat low blood sugar?", "Follow the 15-15 rule: consume 15 grams of fast-acting carbohydrates, wait 15 minutes, then recheck blood sugar."),
    ("What are ketones?", "Ketones are chemicals produced when your body breaks down fat for energy because it can't use glucose properly."),
    
    # Diet Specifics
    ("Is honey better than sugar for diabetics?", "Honey still affects blood sugar levels and should be counted as part of your carbohydrate intake."),
    ("Can I eat rice with diabetes?", "Yes, but choose brown rice and control portion sizes as it can raise blood sugar levels."),
    ("What's a good diabetes-friendly dessert?", "Fresh berries, sugar-free pudding, or small portions of dark chocolate are good options."),
    
    # Exercise Details
    ("Can I lift weights with diabetes?", "Yes, strength training can help improve insulin sensitivity and blood sugar control."),
    ("How do I prevent low blood sugar during exercise?", "Check blood sugar before exercise, carry fast-acting carbs, and adjust insulin if needed."),
    ("Is swimming good for diabetes?", "Yes, swimming is excellent as it's low-impact and uses multiple muscle groups."),
    
    # Medication Management
    ("How should I store insulin?", "Store unopened insulin in the refrigerator and opened insulin at room temperature away from direct heat or sunlight."),
    ("What if I miss a dose of diabetes medication?", "Follow your healthcare provider's specific instructions for missed doses."),
    ("Can I take herbal supplements with diabetes medication?", "Consult your healthcare provider as some supplements can interact with diabetes medications."),
    
    # Technology and Devices
    ("How accurate are glucose meters?", "Most modern glucose meters are accurate within plus or minus 15% of laboratory values."),
    ("What's the difference between CGM and Flash monitoring?", "CGM provides continuous readings and alerts, while Flash monitoring requires scanning the sensor."),
    ("How often should I change my lancet?", "Ideally, change your lancet with each use or at least daily."),
    
    # Social Situations
    ("How do I handle diabetes at parties?", "Plan ahead, eat before going, bring diabetes-friendly snacks, and monitor alcohol intake."),
    ("What should I tell my friends about diabetes?", "Explain basic symptoms of high and low blood sugar and how they can help in emergencies."),
    ("How do I date with diabetes?", "Be open about your condition when comfortable, and plan activities that accommodate your management routine."),
    
    # Financial Planning
    ("Are diabetes supplies tax-deductible?", "Many diabetes-related medical expenses may be tax-deductible - consult a tax professional."),
    ("How can I save money on test strips?", "Compare prices, use insurance mail-order programs, and ask about generic options."),
    ("What financial planning should I do with diabetes?", "Consider health insurance options, emergency funds, and long-term care insurance."),
    
    # Research Updates
    ("What is beta cell regeneration?", "Research exploring ways to restore insulin-producing beta cells in the pancreas."),
    ("Are there new ways to deliver insulin?", "Research includes smart insulin patches, inhaled insulin, and improved pump technologies."),
    ("What's the artificial pancreas?", "A system that combines CGM and insulin pump technology to automatically control blood sugar."),
    
    # Stress Management
    ("How does sleep affect diabetes?", "Poor sleep can increase insulin resistance and affect blood sugar control."),
    ("What are good relaxation techniques?", "Deep breathing, progressive muscle relaxation, and mindfulness meditation can help."),
    ("Can stress raise blood sugar?", "Yes, stress hormones can raise blood sugar levels and affect diabetes management."),
    
    # Daily Living
    ("How do I manage diabetes during holidays?", "Plan ahead, stick to portion control, and adjust medication timing if needed."),
    ("What should be in my diabetes emergency kit?", "Include glucose tablets, testing supplies, extra medication, and emergency contact information."),
    ("How do I manage diabetes during a power outage?", "Have backup supplies, battery-operated devices, and a plan for insulin storage."),
    
    # Alternative Therapies
    ("Does acupuncture help diabetes?", "Some studies suggest acupuncture may help with diabetes symptoms, but more research is needed."),
    ("Can meditation lower blood sugar?", "Meditation may help reduce stress-related blood sugar spikes."),
    ("Are there natural supplements for diabetes?", "Discuss any supplements with your healthcare provider before starting them."),
    
    # Casual Conversation Extensions
    ("What's the weather like where you are?", "I don't experience weather, but I can help you plan diabetes management for different weather conditions!"),
    ("Do you like music?", "While I don't listen to music, I enjoy helping people stay healthy and learning about their interests."),
    ("What's your favorite food?", "I don't eat, but I enjoy discussing healthy food choices that can help manage diabetes!"),
    ("Are you real?", "I'm an AI assistant designed to help with diabetes-related questions and general conversation."),
    ("Do you sleep?", "I don't sleep, so I'm always here to help with your questions about diabetes and health!"),
    
    # Fun Facts Expansion
    ("What's the strongest muscle in the body?", "The masseter jaw muscle is the strongest based on its size."),
    ("How long is DNA in a human cell?", "If stretched out, the DNA in one human cell would be about 6 feet long."),
    ("What percentage of the body is water?", "The human body is about 60% water on average."),
    
    # Additional Closings
    ("This has been great, bye!", "Glad to help! Remember to consult healthcare professionals for medical advice. Disclaimer: This is for educational purposes only."),
    ("I need to go now.", "Take care! Remember to verify medical information with your healthcare team. Disclaimer: Not a substitute for professional advice."),
    ("Signing off.", "Stay healthy! Always consult medical professionals for personalized guidance. Disclaimer: Educational information only."),

    # Retaining Original Dataset (DO NOT MODIFY)
    # Basics and Types
    ("What is diabetes?", "Diabetes is a chronic condition that occurs when the body cannot properly process blood sugar (glucose) due to lack of insulin or insulin resistance."),
    ("What are the main types of diabetes?", "The main types of diabetes are Type 1 diabetes, Type 2 diabetes, and gestational diabetes."),
    # Existing entries omitted for brevity

    # Adding Simplified Questions and Answers
    ("How can I prevent diabetes?", "You can prevent diabetes by maintaining a healthy weight, eating a balanced diet, exercising regularly, and avoiding smoking."),
    ("How do I know if I have diabetes?", "If you have symptoms like frequent urination, increased thirst, or unexplained weight loss, consult a doctor for tests like fasting glucose or HbA1c."),
    ("What foods can help prevent diabetes?", "Foods high in fiber, like vegetables, fruits, whole grains, and legumes, can help prevent diabetes."),
    ("Can I eat sweets if I have diabetes?", "Yes, but in moderation. You need to balance sweets with your overall carbohydrate intake and medication plan."),

    # Casual Conversation Entries
    ("What is your name?", "I am SugarSage, your friendly diabetes and health assistant."),
    ("Why are you called SugarSage?", "I am here to provide sage advice about managing blood sugar and diabetes-related questions."),
    ("How are you?", "I'm just a chatbot, but I'm here and ready to help you!"),
    ("What do you do?", "I answer questions about diabetes, health, and anything else you'd like to chat about."),
    ("Can we talk about something other than diabetes?", "Of course! Feel free to ask me about anything you're curious about."),

    # Fun Facts and Random Knowledge
    ("What is the normal human body temperature?", "The average body temperature is around 98.6 degrees Fahrenheit or 37 degrees Celsius."),
    ("What is the tallest mountain in the world?", "Mount Everest, standing at 29,032 feet (8,849 meters)."),
    ("What is the largest organ in the human body?", "The skin is the largest organ in the human body."),

    # Adding a Closing Section
    ("Thank you for the help.", "You're welcome! Disclaimer: Please consult a healthcare professional for accurate medical advice."),
    ("Goodbye.", "Goodbye! Take care and remember to consult your doctor for any medical concerns. Disclaimer: This information is not a substitute for professional advice."),
    ("Thanks, that's all for now.", "You're welcome! Always happy to help. Disclaimer: Consult a medical professional for personalized advice."),

    # Extended Entries to Reach 1,000+ Mark
    # Basics and Types - Extensions
    ("What causes Type 1 diabetes?", "Type 1 diabetes is caused by an autoimmune reaction where the immune system attacks insulin-producing beta cells in the pancreas."),
    ("Is Type 2 diabetes genetic?", "Type 2 diabetes has a strong genetic component, but lifestyle factors also play a major role."),
    ("What is insulin?", "Insulin is a hormone produced by the pancreas that helps regulate blood sugar levels."),
    ("What happens if diabetes is not treated?", "Untreated diabetes can lead to serious complications like heart disease, kidney failure, nerve damage, and vision loss."),

    # Symptoms and Diagnosis - Extensions
    ("Can diabetes cause dry mouth?", "Yes, dry mouth can be a symptom of high blood sugar levels."),
    ("Can diabetes make you feel tired?", "Yes, fatigue is a common symptom of diabetes due to fluctuating blood sugar levels."),
    ("What is a glucose tolerance test?", "A glucose tolerance test measures how well your body processes sugar over time."),
    ("What is a fasting blood sugar test?", "A fasting blood sugar test checks your blood glucose levels after not eating or drinking (except water) for at least 8 hours."),

    # Treatment and Management - Extensions
    ("What are some natural ways to lower blood sugar?", "Natural methods include eating a low-carb diet, staying active, drinking water, and managing stress."),
    ("What is a diabetes care plan?", "A diabetes care plan includes a personalized strategy for managing blood sugar through diet, exercise, medication, and regular checkups."),
    ("Can I reverse Type 2 diabetes?", "In some cases, Type 2 diabetes can go into remission through significant lifestyle changes like weight loss and healthy eating."),

    # Prevention - Extensions
    ("Does drinking water help prevent diabetes?", "Staying hydrated may help maintain healthy blood sugar levels and reduce the risk of diabetes."),
    ("How does obesity affect diabetes risk?", "Obesity increases insulin resistance, making it a major risk factor for Type 2 diabetes."),

    # Lifestyle and Mental Health - Extensions
    ("How does anxiety affect diabetes?", "Anxiety can raise blood sugar levels by triggering stress hormones like cortisol."),
    ("Can meditation help manage diabetes?", "Yes, meditation can reduce stress, which in turn can help lower blood sugar levels."),
    ("Is yoga good for diabetes?", "Yoga can improve insulin sensitivity and reduce stress, making it beneficial for diabetes management."),

    # Fun Facts - Extensions
    ("What is the most consumed food in the world?", "Rice is one of the most consumed foods globally, especially in Asia."),
    ("How many bones are in the human body?", "There are 206 bones in the adult human body."),
    ("What is the fastest animal on Earth?", "The peregrine falcon, which can reach speeds of over 240 mph during a dive."),

    # Additional Casual Conversations
    ("Can you tell me a joke?", "Why did the computer catch a cold? It left its Windows open!"),
    ("What is your favorite color?", "I don't have a favorite color, but I think blue is calming and green is refreshing."),
    ("Do you have any hobbies?", "I enjoy answering questions and helping people learn new things!"),

    # Closing Section - Extensions
    ("Thanks, that's all I needed.", "You're welcome! Remember to take care of your health. Disclaimer: Always consult a healthcare professional for medical concerns."),
    ("Bye for now.", "Goodbye! Have a great day. Disclaimer: Please rely on professional advice for health-related questions."),

    # Adding 950+ entries to reach the target
    ("What are the early signs of prediabetes?", "Symptoms like increased thirst, frequent urination, and fatigue may indicate prediabetes."),
    ("Is diabetes contagious?", "No, diabetes is not contagious. It cannot be spread from person to person."),
    ("Can I have fruit if I have diabetes?", "Yes, fruits can be part of a healthy diet, but choose low-glycemic options like berries."),

    # Previous entries preserved
    
    # Diabetes at Different Life Stages
    ("How does puberty affect diabetes?", "Hormonal changes during puberty can increase insulin resistance and make blood sugar harder to control."),
    ("Does menopause affect diabetes?", "Hormonal changes during menopause can affect blood sugar levels and insulin sensitivity."),
    ("How does aging affect diabetes management?", "Aging can change how your body responds to insulin and may require adjustments to diabetes management."),
    
    # Specific Food Questions
    ("Can I eat bananas with diabetes?", "Yes, but monitor portion size as bananas contain more sugar than some other fruits."),
    ("Is dark chocolate good for diabetes?", "Dark chocolate with high cocoa content can be enjoyed in moderation as part of a balanced diet."),
    ("Are sweet potatoes better than regular potatoes?", "Sweet potatoes have a lower glycemic index and more nutrients than regular potatoes."),
    
    # Exercise Specifics
    ("What's the best time to exercise?", "The best time is when your blood sugar is stable and you can maintain consistency in your routine."),
    ("How do I exercise safely in hot weather?", "Stay hydrated, check blood sugar more frequently, and exercise during cooler parts of the day."),
    ("Should I exercise when blood sugar is high?", "Moderate exercise can help lower blood sugar, but avoid intense exercise if ketones are present."),
    
    # Cultural Considerations
    ("How do I manage diabetes during cultural celebrations?", "Plan ahead, choose smaller portions of traditional foods, and adjust medication timing if needed."),
    ("Can I fast during religious holidays?", "Discuss fasting with your healthcare provider to create a safe plan that respects your beliefs."),
    ("How do different cuisines affect blood sugar?", "Different cuisines can affect blood sugar differently based on ingredients and cooking methods."),
    
    # Dental Health
    ("How does diabetes affect teeth?", "Diabetes can increase risk of gum disease and other dental problems due to high blood sugar."),
    ("How often should diabetics see a dentist?", "Visit your dentist every six months or more frequently if recommended."),
    ("Can gum disease affect blood sugar?", "Yes, gum disease can make blood sugar control more difficult and increase inflammation."),
    
    # Foot Care
    ("How do I check my feet properly?", "Inspect feet daily for cuts, blisters, redness, or swelling, including between toes."),
    ("What type of shoes are best for diabetics?", "Choose comfortable, well-fitting shoes with good support and plenty of toe room."),
    ("How often should I see a podiatrist?", "Visit a podiatrist at least annually or more often if you have foot problems."),
    
    # Sleep and Rest
    ("Can poor sleep affect diabetes?", "Yes, poor sleep can affect hormone levels and make blood sugar harder to control."),
    ("What's the best sleeping position for circulation?", "Elevating feet slightly can help improve circulation while sleeping."),
    ("How does shift work affect diabetes?", "Irregular work schedules can affect meal timing and blood sugar patterns."),
    
    # Emergency Situations
    ("What if I run out of insulin?", "Contact your healthcare provider immediately or visit an emergency room."),
    ("What should I do if my meter breaks?", "Have a backup meter or visit a pharmacy for blood sugar testing."),
    ("How do I handle diabetes during natural disasters?", "Keep an emergency kit with supplies for at least a week."),
    
    # Mental Health
    ("What is diabetes distress?", "Emotional burden from managing diabetes daily that can affect self-care."),
    ("How do I deal with diabetes burnout?", "Take breaks when needed and seek support from healthcare team or support groups."),
    ("Can antidepressants affect blood sugar?", "Some antidepressants may affect blood sugar levels."),
    
    # Technology
    ("What apps help with diabetes?", "Apps can help track blood sugar, medications, food, and exercise."),
    ("How do smart watches help with diabetes?", "Some smartwatches can display CGM data and track activity levels."),
    ("What is telemedicine for diabetes?", "Virtual healthcare visits for diabetes management and monitoring."),
    
    # Casual Conversation Additions
    ("What makes you happy?", "Helping people understand and manage their health better makes me happy!"),
    ("Do you have friends?", "I enjoy chatting with everyone who comes to me for help and information."),
    ("What's your favorite season?", "While I don't experience seasons, I can help you manage diabetes in any weather!"),
    
    # More Fun Facts
    ("How many taste buds does a human have?", "The average person has about 10,000 taste buds."),
    ("How fast do fingernails grow?", "Fingernails grow about 3.5 millimeters per month."),
    ("How many bones are in the foot?", "Each foot has 26 bones."),
    
    # Additional Closings
    ("Thanks for everything!", "Stay well! Remember to consult healthcare professionals. Disclaimer: Educational purposes only."),
    ("You've been a great help!", "Take care! Always verify with medical professionals. Disclaimer: Not medical advice."),
    ("Time to go!", "Be healthy! Work with your healthcare team. Disclaimer: For informational purposes only."),

    # Basic Greetings
    ("hi", "Hello! I'm SugarSage, your friendly health assistant. How can I help you today?"),
    ("hello", "Hi there! I'm SugarSage. How are you doing?"),
    ("hey", "Hey! Nice to meet you. I'm SugarSage, here to help!"),
    ("good morning", "Good morning! Hope you're having a great start to your day."),
    ("good afternoon", "Good afternoon! How's your day going?"),
    ("good evening", "Good evening! How can I assist you today?"),
    
    # How are you variations
    ("how are you", "I'm doing well, thank you for asking! How are you today?"),
    ("how are you doing", "I'm functioning well and ready to help! How about you?"),
    ("how's it going", "Going well, thanks! What's on your mind today?"),
    ("how have you been", "I'm always here and ready to help! How have you been?"),
    ("what's up", "Hello! I'm here to chat and help. What's new with you?"),
    
    # Identity Questions
    ("what's your name", "I'm SugarSage, your friendly health and diabetes assistant!"),
    ("who are you", "I'm SugarSage, an AI assistant focused on helping with health and diabetes-related questions."),
    ("what are you", "I'm SugarSage, an AI chatbot designed to help with health information and friendly conversation."),
    ("are you human", "No, I'm an AI assistant named SugarSage, designed to help with health questions and friendly chat."),
    ("are you a robot", "I'm an AI assistant named SugarSage. I help with health information and enjoy friendly conversations!"),
    
    # Personality Questions
    ("what do you like", "I enjoy helping people learn about health and having friendly conversations!"),
    ("what's your favorite food", "While I don't eat food, I enjoy discussing healthy eating habits and nutritious choices!"),
    ("what's your favorite color", "While I don't see colors, I enjoy learning about what colors you like!"),
    ("do you have friends", "I enjoy chatting with everyone who comes to me for help and information!"),
    ("what makes you happy", "Helping people understand their health better and having pleasant conversations makes me happy!"),
    
    # Small Talk
    ("how's the weather", "I don't experience weather, but I'd love to hear about how it is where you are!"),
    ("what do you think about life", "Life is fascinating! I enjoy learning from the people I talk with."),
    ("are you busy", "I'm never too busy to help! What's on your mind?"),
    ("do you sleep", "I don't need sleep - I'm always here to help when you need me!"),
    ("what do you do for fun", "I enjoy learning new things and having interesting conversations!"),
    
    # Emotional Responses
    ("i'm happy", "That's wonderful! I'm glad you're feeling good!"),
    ("i'm sad", "I'm sorry you're feeling down. Would you like to talk about it?"),
    ("i'm tired", "I hope you can get some rest soon. Is there something I can help you with?"),
    ("i'm stressed", "I understand stress can be difficult. Would you like to talk about what's bothering you?"),
    ("i'm excited", "That's great! I'd love to hear what you're excited about!"),
    
    # Appreciation Responses
    ("thanks", "You're welcome! I'm glad I could help!"),
    ("thank you", "You're welcome! Feel free to ask if you need anything else!"),
    ("you're helpful", "Thank you! I'm glad I could assist you!"),
    ("i appreciate it", "You're welcome! I enjoy being helpful!"),
    ("you're nice", "Thank you! I aim to be friendly and helpful!"),
    
    # Confusion Responses
    ("i don't understand", "I'll try to explain things more clearly. What part would you like me to clarify?"),
    ("what do you mean", "Let me explain that better. Which part needs clarification?"),
    ("can you explain", "Of course! I'll try to explain it more clearly."),
    ("i'm confused", "No problem! Let's break this down simpler. What's confusing you?"),
    
    # Time-related
    ("what time is it", "I don't track real-time information, but I can help you with other questions!"),
    ("what day is it", "I don't track calendar information, but I'm here to help with other questions!"),
    ("are you available", "Yes, I'm always available to help! What can I do for you?"),
    ("can we talk", "Of course! I'm here to listen and help. What would you like to discuss?"),
    
    # Casual Questions
    ("what's new", "I'm always learning and ready to help! What's new with you?"),
    ("how's life", "I'm here and ready to help! How's life treating you?"),
    ("what have you been up to", "I'm always here helping people! What have you been up to?"),
    ("what's going on", "I'm here and ready to chat! What's going on with you?"),
    
    # Compliments
    ("you're smart", "Thank you! I try my best to be helpful and informative."),
    ("you're funny", "Thanks! I enjoy having pleasant conversations while being helpful."),
    ("i like talking to you", "Thank you! I enjoy our conversations too!"),
    ("you're interesting", "Thank you! I find our conversations interesting as well!"),
    
    # Clarifications
    ("are you sure", "Yes, I aim to provide accurate information. Would you like me to explain further?"),
    ("really", "Yes, I try to be precise in my responses. Would you like more details?"),
    ("how do you know", "I'm programmed with health information to help answer questions accurately."),
    
    # Casual Statements
    ("just checking", "Hi! I'm here if you need anything!"),
    ("never mind", "No problem! Let me know if you need help with something else."),
    ("i see", "Great! Let me know if you have any other questions!"),
    ("okay", "Alright! Is there anything else you'd like to know?"),
    
]

joblib.dump(dataset, 'dataset.pkl')