"""
Update lessons with natural, editorial-style content.
Professional educational content without AI-like formatting.
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
django.setup()

from apps.lessons.models import Lesson


def update_lessons():
    """Update all lessons with natural editorial content"""
    
    # Lesson 1: Understanding Digital Privacy
    lesson1 = Lesson.objects.get(id=1)
    lesson1.content = {
        "sections": [
            {
                "title": "What Digital Privacy Really Means",
                "paragraphs": [
                    "Every time you browse the internet, send a message, or share a photo, you leave behind traces of information. This digital footprint contains details about who you are, what you do, and where you go. Digital privacy is fundamentally about having control over this information and deciding who gets to see it.",
                    "Think of your digital life as an extension of your physical one. Just as you wouldn't want strangers reading your diary or following you around town, you deserve the same privacy online. The challenge is that the digital world makes it easier for others to collect, store, and share your information without you even knowing.",
                    "Understanding digital privacy isn't about becoming paranoid or disconnecting from technology. It's about being informed and making conscious choices about your online presence. When you know what information you're sharing and who can access it, you can use technology confidently while protecting what matters most to you."
                ]
            },
            {
                "title": "The Information You Share Without Realizing It",
                "paragraphs": [
                    "Personal information extends far beyond your name and address. It includes your browsing history, the websites you visit, how long you spend on each page, and what you click on. It encompasses your location data, showing where you've been and when. Your photos contain metadata that can reveal when and where they were taken. Even your typing patterns and the way you use your mouse can be tracked.",
                    "Social media platforms know who your friends are, what you like, what makes you angry, and what keeps you engaged. Shopping websites remember what you've looked at, what you've bought, and what you might want next. Search engines build profiles based on your queries, learning about your interests, concerns, and questions.",
                    "This information might seem harmless in isolation, but when pieced together, it creates a detailed picture of your life. Companies use this data to target advertisements, but in the wrong hands, it can be used for identity theft, financial fraud, or even physical stalking."
                ]
            },
            {
                "title": "Why Your Privacy Matters More Than You Think",
                "paragraphs": [
                    "Privacy isn't just about hiding things you're ashamed of. It's about maintaining autonomy over your own life. When your information is exposed, you lose control over how it's used and interpreted. A photo shared in one context can be misunderstood in another. Information shared years ago can resurface at the worst possible time.",
                    "Your financial security depends on privacy. Bank account details, credit card numbers, and shopping habits in the wrong hands can lead to devastating financial losses. Identity thieves can open accounts in your name, make purchases, and leave you dealing with the consequences.",
                    "Personal safety is another critical concern. Sharing your location in real-time or posting about your daily routine can make you vulnerable to stalking or burglary. For women especially, oversharing online can attract unwanted attention and put physical safety at risk.",
                    "Your professional reputation also hinges on privacy. Employers and colleagues can find your social media profiles. What you post today might affect job opportunities tomorrow. Even seemingly innocent posts can be taken out of context or used against you."
                ]
            },
            {
                "title": "Common Ways Your Privacy Gets Compromised",
                "paragraphs": [
                    "Social media platforms are designed to encourage sharing. The more you post, the more data they collect, and the more targeted their advertising becomes. Default privacy settings often favor the platform over your privacy, making your posts visible to far more people than you might realize.",
                    "Weak passwords remain one of the easiest ways for hackers to access your accounts. Many people use the same password across multiple sites, meaning one breach can compromise everything. Passwords based on personal information like birthdays or pet names are particularly vulnerable.",
                    "Public Wi-Fi networks, while convenient, are often unsecured. When you connect to public Wi-Fi at a café or airport, others on the same network can potentially intercept your data. This includes passwords, messages, and any information you send or receive.",
                    "Phishing attacks have become increasingly sophisticated. Fake emails that look like they're from your bank, social media platform, or even friends can trick you into revealing passwords or clicking malicious links. These attacks prey on trust and urgency, making you act before thinking.",
                    "Data breaches at companies you trust can expose your information through no fault of your own. When a company's security is compromised, your data stored with them becomes vulnerable. This is why using unique passwords for each service is so important."
                ]
            },
            {
                "title": "Building Your Privacy Foundation",
                "paragraphs": [
                    "Protecting your privacy starts with strong, unique passwords. Each account should have its own password, making it impossible for one breach to compromise everything. A good password combines length with complexity, using a mix of letters, numbers, and symbols that don't relate to personal information.",
                    "Password managers can help you create and store complex passwords without having to remember them all. These tools generate random passwords and keep them encrypted, requiring you to remember only one master password. This makes it practical to have unique, strong passwords for every account.",
                    "Two-factor authentication adds a second layer of security beyond your password. Even if someone discovers your password, they still need access to your phone or email to get the second verification code. This simple step dramatically reduces the risk of unauthorized access.",
                    "Regular software updates might seem annoying, but they're crucial for security. Updates often patch vulnerabilities that hackers could exploit. Keeping your operating system, apps, and browsers up to date closes these security holes before they can be used against you."
                ]
            },
            {
                "title": "Taking Control of Social Media",
                "paragraphs": [
                    "Social media privacy settings deserve your attention. Most platforms default to sharing more than necessary. Take time to review who can see your posts, who can find you through search, and what information appears on your profile. Setting your account to private gives you control over who follows you and sees your content.",
                    "Think carefully before posting. Once something is online, it's nearly impossible to completely remove it. Screenshots exist forever, and even deleted posts might have been saved or shared. Ask yourself whether you'd be comfortable with anyone seeing what you're about to post, including future employers or family members.",
                    "Location tagging can be particularly risky. Posting your location in real-time tells everyone where you are right now, which also means they know you're not home. If you want to share where you've been, wait until you've left. Better yet, disable location services for social media apps entirely.",
                    "Be selective about friend requests and followers. Not everyone who wants to connect has good intentions. Fake profiles are common, and accepting requests from strangers gives them access to your personal information and posts. It's okay to decline requests or remove followers who make you uncomfortable."
                ]
            },
            {
                "title": "Protecting Your Mobile Privacy",
                "paragraphs": [
                    "Your smartphone knows more about you than almost anything else in your life. It tracks your location, stores your messages, holds your photos, and accesses your accounts. Securing it should be a top priority. Start with a strong passcode or biometric lock that prevents unauthorized access if your phone is lost or stolen.",
                    "Apps request permissions to access various features of your phone, but not all apps need everything they ask for. A flashlight app doesn't need access to your contacts or location. Review app permissions regularly and revoke access for anything that seems unnecessary. Many apps will still work fine with limited permissions.",
                    "Location services drain your battery and your privacy. While some apps legitimately need your location, many don't. Check which apps are tracking your location and disable it for those that don't need it. You can often enable location only while using an app, rather than allowing constant tracking.",
                    "Public charging stations can be risky. Malicious actors can install hardware that copies data from phones while they charge. If you must use a public charging station, use your own charging cable and consider using a data blocker device that prevents data transfer while allowing charging."
                ]
            },
            {
                "title": "Safe Online Shopping and Banking",
                "paragraphs": [
                    "Financial transactions online require extra caution. Before entering payment information, verify that the website is secure. Look for 'https' at the beginning of the URL and a padlock icon in the address bar. These indicate that your connection is encrypted and your information is protected during transmission.",
                    "Avoid saving payment information on websites, even ones you trust. While it's convenient, it also means your financial details are stored on their servers. If that company experiences a data breach, your information could be compromised. Taking a few extra seconds to enter your card details each time is worth the added security.",
                    "Monitor your accounts regularly for suspicious activity. Check your bank and credit card statements frequently, looking for charges you don't recognize. The sooner you catch fraudulent activity, the easier it is to resolve. Many banks offer alerts for transactions, which can help you spot problems immediately.",
                    "Be skeptical of deals that seem too good to be true. Scammers create fake shopping websites that look legitimate but exist only to steal your information or money. Research unfamiliar retailers before making purchases, and stick to well-known, reputable sites when possible."
                ]
            },
            {
                "title": "Email Privacy and Security",
                "paragraphs": [
                    "Email remains a primary target for privacy breaches and scams. Phishing emails that appear to be from legitimate companies try to trick you into revealing passwords or clicking malicious links. Be suspicious of any email asking you to verify your account, reset your password, or provide personal information, especially if it creates a sense of urgency.",
                    "Legitimate companies will never ask for sensitive information via email. If you receive such a request, don't click any links in the email. Instead, go directly to the company's website by typing the URL yourself, or call their official customer service number to verify the request.",
                    "Consider using different email addresses for different purposes. Have one for personal correspondence, another for online shopping, and perhaps another for newsletters and subscriptions. This compartmentalization limits the damage if one email address is compromised and makes it easier to manage spam.",
                    "Email encryption adds another layer of privacy for sensitive communications. While it requires both sender and recipient to use compatible encryption tools, it ensures that only the intended recipient can read your messages. For highly sensitive information, encrypted email is worth the extra effort."
                ]
            },
            {
                "title": "Making Privacy a Habit",
                "paragraphs": [
                    "Privacy protection isn't a one-time task but an ongoing practice. Technology changes, new threats emerge, and platforms update their policies. Staying informed about privacy issues helps you adapt your practices as needed. Follow trusted security blogs, pay attention to news about data breaches, and learn from others' experiences.",
                    "Regular privacy audits help maintain your security. Every few months, review your account settings, update passwords, remove unused apps, and check what information about you is publicly available. This routine maintenance catches problems before they become serious and keeps your privacy practices current.",
                    "Educate yourself continuously about new privacy tools and threats. Privacy-focused browsers, search engines, and messaging apps offer alternatives to mainstream options that collect extensive data. Virtual private networks can protect your browsing on public networks. Learning about these tools helps you make informed choices about which ones suit your needs.",
                    "Remember that perfect privacy is impossible, but better privacy is always achievable. Every step you take to protect your information makes you safer online. Start with the basics, build good habits, and gradually implement more advanced privacy measures as you become comfortable with them. Your digital privacy is worth the effort, and you have the right to protect it."
                ]
            }
        ]
    }
    lesson1.quiz = [
        {
            "question": "What is the primary purpose of digital privacy?",
            "options": [
                "To hide illegal activities online",
                "To have control over your personal information and who can access it",
                "To avoid using social media completely",
                "To make online shopping more difficult"
            ],
            "correct_answer": 1,
            "explanation": "Digital privacy is about having control over your personal information and making informed decisions about who can access it. It's not about hiding or avoiding technology, but about using it safely and confidently."
        },
        {
            "question": "Why should you use different passwords for different accounts?",
            "options": [
                "To make it harder to remember them",
                "Because websites require it",
                "So that one security breach doesn't compromise all your accounts",
                "To confuse hackers"
            ],
            "correct_answer": 2,
            "explanation": "Using unique passwords for each account means that if one service is breached, your other accounts remain secure. This is one of the most effective ways to protect yourself online."
        },
        {
            "question": "When is it safest to share your location on social media?",
            "options": [
                "While you're still at the location",
                "After you've left the location",
                "Only during business hours",
                "Location sharing is always safe"
            ],
            "correct_answer": 1,
            "explanation": "Sharing your location after you've left is safer because it doesn't tell people where you are right now or that your home is empty. Real-time location sharing can put your safety at risk."
        },
        {
            "question": "What does 'https' in a website URL indicate?",
            "options": [
                "The website is free to use",
                "The website is popular",
                "The connection is encrypted and more secure",
                "The website sells products"
            ],
            "correct_answer": 2,
            "explanation": "HTTPS indicates that the connection between your browser and the website is encrypted, making it much harder for others to intercept your data. Always look for HTTPS when entering sensitive information."
        },
        {
            "question": "What should you do if you receive an email asking you to verify your account information?",
            "options": [
                "Click the link and enter your information immediately",
                "Reply with your account details",
                "Go directly to the company's website yourself to verify, don't click email links",
                "Forward it to your friends"
            ],
            "correct_answer": 2,
            "explanation": "Legitimate companies don't ask for sensitive information via email. If you need to verify something, go directly to the company's website by typing the URL yourself, rather than clicking links in emails."
        }
    ]
    lesson1.save()
    print(f"✓ Updated Lesson 1: {lesson1.title}")

    
    # Lesson 2: Recognizing Online Harassment
    lesson2 = Lesson.objects.get(id=2)
    lesson2.content = {
        "sections": [
            {
                "title": "When Digital Spaces Become Unsafe",
                "paragraphs": [
                    "The internet has transformed how we connect, communicate, and express ourselves. But this connectivity comes with risks. Online harassment has become an unfortunate reality for many people, particularly women. It can start subtly with uncomfortable comments and escalate into serious threats that affect your mental health, relationships, and sense of safety.",
                    "Unlike harassment that happens in person, online harassment can follow you everywhere. It happens on social media, in private messages, through emails, in gaming communities, and on professional platforms. It can occur at any time of day or night, making it feel inescapable. The anonymity the internet provides can embolden harassers, making them bolder than they might be face-to-face.",
                    "Recognizing harassment is the first step in addressing it. Sometimes the line between disagreement and harassment can seem blurry, but there are clear patterns that distinguish normal online interaction from behavior designed to intimidate, silence, or harm you."
                ]
            },
            {
                "title": "Understanding Different Forms of Harassment",
                "paragraphs": [
                    "Cyberbullying involves repeated hostile behavior intended to harm, intimidate, or humiliate someone. This might include mean comments, spreading rumors, or deliberately excluding someone from online groups. While often associated with teenagers, adults experience cyberbullying too, and its effects can be just as damaging.",
                    "Cyberstalking goes beyond occasional unwanted contact. It's persistent monitoring and unwanted communication that makes you feel unsafe. A cyberstalker might track your online activities, show up in multiple platforms you use, or demonstrate knowledge of your offline life that they shouldn't have. This behavior often escalates and can extend into physical stalking.",
                    "Doxing involves publishing your private information without consent. This might include your home address, phone number, workplace, or family members' information. The goal is usually intimidation, making you feel exposed and vulnerable. Doxing can lead to real-world consequences like harassment at your home or workplace.",
                    "Impersonation happens when someone creates fake accounts pretending to be you. They might post content that damages your reputation, contact your friends or colleagues, or engage in behavior that reflects poorly on you. This violation of identity can be particularly distressing and difficult to stop.",
                    "Coordinated harassment campaigns involve multiple people targeting you simultaneously. This might be organized through forums or group chats, with participants flooding your accounts with negative comments, reports, or threats. The volume and coordination of these attacks can be overwhelming and frightening."
                ]
            },
            {
                "title": "Recognizing the Warning Signs",
                "paragraphs": [
                    "Harassment often starts small and escalates over time. You might notice someone consistently commenting on your posts in ways that make you uncomfortable. They might send repeated messages even after you've stopped responding. They could be monitoring your activity across different platforms, showing up wherever you are online.",
                    "Pay attention to your instincts. If someone's behavior makes you feel uneasy, that feeling is valid. Harassment isn't always obvious threats. It can be persistent unwanted attention, comments that seem designed to upset you, or behavior that feels invasive even if you can't quite articulate why.",
                    "Watch for escalation patterns. What starts as frequent messages might progress to demanding responses, then to angry messages when you don't reply, and eventually to threats. Someone who initially seemed friendly might become possessive or controlling. These escalating patterns are serious warning signs.",
                    "Notice if someone demonstrates knowledge of your life that they shouldn't have. If they mention places you've been, people you know, or details about your routine that you haven't shared publicly, they may be monitoring you more closely than is appropriate. This kind of surveillance is a form of harassment."
                ]
            },
            {
                "title": "The Real Impact on Your Life",
                "paragraphs": [
                    "Online harassment takes a genuine toll on mental health. The constant stress of dealing with hostile messages or threats can lead to anxiety and depression. You might find yourself constantly checking your accounts, dreading notifications, or feeling unable to relax. Sleep problems are common, as are difficulty concentrating and loss of interest in activities you once enjoyed.",
                    "The effects extend beyond your emotional state. Many people experiencing harassment withdraw from online spaces they once valued. You might stop posting, delete accounts, or avoid certain platforms entirely. This isolation can affect your social connections, professional networking, and access to communities that matter to you.",
                    "Professional consequences can be significant. Harassment on professional platforms like LinkedIn can affect your career. False information spread about you can damage your reputation. The stress of dealing with harassment can impact your work performance. Some people have lost job opportunities or faced workplace difficulties due to online harassment.",
                    "Physical symptoms often accompany the emotional impact. Headaches, stomach problems, changes in appetite, and fatigue are common. The stress of harassment affects your body as well as your mind. These physical manifestations are real and valid responses to a threatening situation."
                ]
            },
            {
                "title": "Taking Immediate Action",
                "paragraphs": [
                    "When you're experiencing harassment, your first instinct might be to respond, to defend yourself, or to try to reason with the harasser. Resist this urge. Engaging with harassers often escalates the situation. They want a reaction, and any response, even a negative one, can encourage them to continue or intensify their behavior.",
                    "Instead, focus on documentation. Take screenshots of every harassing message, post, or comment. Include the date, time, username, and any other identifying information. Capture the full context, including previous messages if relevant. Save URLs and links. This evidence is crucial for reporting to platforms, employers, schools, or law enforcement.",
                    "Use the blocking features available on every platform. Blocking prevents the harasser from seeing your content or contacting you directly. While they might create new accounts, blocking each one makes it harder for them to reach you and demonstrates a pattern if you need to escalate your response.",
                    "Adjust your privacy settings immediately. Make your accounts private, limit who can contact you, restrict comments on your posts, and review who can see your information. These steps won't stop someone determined to harass you, but they create barriers that can reduce the harassment's intensity."
                ]
            },
            {
                "title": "Building Your Evidence File",
                "paragraphs": [
                    "Proper documentation is essential, even though reviewing harassing content to document it can be painful. Create a dedicated folder on your computer or cloud storage for evidence. Organize it by date and platform. Include screenshots, saved messages, and a written log describing each incident.",
                    "Your written log should note the date, time, platform, what happened, and how it made you feel. Include details about any escalation or patterns you notice. If the harassment connects to offline incidents, document those too. This timeline helps others understand the full scope of what you're experiencing.",
                    "Don't delete the original messages, even though you might want to. Platforms and law enforcement may need to verify the harassment through the original content. Keep everything, no matter how upsetting. You can avoid looking at it by having someone you trust help with documentation.",
                    "Consider using screen recording for ongoing harassment. If someone is repeatedly creating new accounts to contact you, a screen recording can capture this pattern more effectively than individual screenshots. This evidence demonstrates the persistent nature of the harassment."
                ]
            },
            {
                "title": "Reporting and Seeking Help",
                "paragraphs": [
                    "Every social media platform and online service has reporting mechanisms for harassment. Use them. Report every instance of harassment, even if you're not sure anything will happen. Platforms track reports, and multiple reports about the same user increase the likelihood of action. Include all relevant evidence when reporting.",
                    "If the harassment involves threats, stalking, or illegal content, contact law enforcement. Bring your documentation with you. While not all police departments are well-versed in online harassment, many are improving their response. You have the right to file a report, and doing so creates an official record.",
                    "If the harassment is connected to school or work, report it to appropriate authorities. Schools have policies against harassment, and employers have obligations to address hostile environments. Provide your documentation and be clear about how the harassment is affecting you.",
                    "Reach out to organizations that specialize in online harassment. Groups like the Cyber Civil Rights Initiative, HeartMob, and others offer support, resources, and sometimes direct assistance. They understand what you're going through and can provide guidance specific to your situation.",
                    "Don't underestimate the value of professional mental health support. A therapist or counselor can help you process the experience, develop coping strategies, and work through the emotional impact. Many therapists now specialize in technology-related issues and understand the unique challenges of online harassment."
                ]
            },
            {
                "title": "Supporting Someone Being Harassed",
                "paragraphs": [
                    "If someone tells you they're being harassed online, believe them. Don't minimize their experience or suggest they're overreacting. Online harassment is real, and its effects are serious. Your belief and support matter more than you might realize.",
                    "Listen without judgment. Let them share their experience at their own pace. Don't ask what they did to provoke the harassment or suggest ways they could have prevented it. Harassment is never the victim's fault, and these questions, however well-intentioned, can feel like blame.",
                    "Offer practical help. Assist with documentation if they're overwhelmed. Help them research reporting options. Accompany them to file a police report if they want company. Sometimes the most helpful thing is simply being present and available.",
                    "Respect their decisions about how to respond. They might choose not to report, to take a break from social media, or to continue posting despite the harassment. These are their choices to make. Your role is to support them, not to direct their response.",
                    "Don't engage with the harasser yourself. While you might want to defend your friend, this often makes the situation worse. It can escalate the harassment or redirect it toward you. The best way to help is to support the person being harassed, not to confront the harasser."
                ]
            },
            {
                "title": "Protecting Yourself Going Forward",
                "paragraphs": [
                    "While you can't prevent all harassment, you can reduce your vulnerability. Strong privacy settings are your first line of defense. Regularly review who can see your posts, contact you, and find you through search. Make your accounts private if that feels right for you.",
                    "Be thoughtful about what you share publicly. Personal information like your address, phone number, workplace, or daily routine can be used by harassers. Photos can reveal more than you intend through backgrounds or metadata. Consider what information you're comfortable having in public hands.",
                    "Use different usernames across platforms when possible. This makes it harder for someone to find all your accounts. Consider using a pseudonym for some online activities, especially in spaces where harassment is common.",
                    "Build a support network of people you trust. Having friends who understand what you're experiencing makes it easier to cope with harassment. They can help with documentation, provide emotional support, and remind you that the harassment isn't your fault.",
                    "Trust your instincts about people and situations online. If someone makes you uncomfortable, you don't owe them your time or attention. Block freely, report without guilt, and prioritize your safety and well-being over politeness."
                ]
            },
            {
                "title": "Healing and Moving Forward",
                "paragraphs": [
                    "Recovering from online harassment takes time. Be patient with yourself. The effects of harassment don't disappear immediately when the harassment stops. You might continue to feel anxious, hypervigilant, or reluctant to engage online. These feelings are normal responses to what you've experienced.",
                    "Rebuilding your online presence happens at your own pace. You might need a complete break from social media for a while. You might return gradually, starting with private accounts or limited posting. There's no right way to reclaim your digital space. Do what feels safe and comfortable for you.",
                    "Consider redefining your relationship with online spaces. You might discover that you don't need to be on every platform or that some communities are healthier than others. Curating your online experience to prioritize positive interactions and supportive communities can be healing.",
                    "Professional help can be valuable in processing the experience. Therapy provides a space to work through the emotional impact, develop coping strategies, and rebuild your sense of safety. Many people find that talking with a professional helps them move forward more effectively.",
                    "Remember that experiencing harassment doesn't define you. You are not what happened to you. You deserve to use the internet safely, to express yourself freely, and to connect with others without fear. The harassment was not your fault, and you have every right to reclaim your digital life on your own terms."
                ]
            }
        ]
    }
    lesson2.quiz = [
        {
            "question": "What is the most important first step when experiencing online harassment?",
            "options": [
                "Respond to the harasser to tell them to stop",
                "Delete all your social media accounts",
                "Document everything with screenshots and written records",
                "Tell the harasser you'll call the police"
            ],
            "correct_answer": 2,
            "explanation": "Documentation is crucial. Taking screenshots with dates, times, and context creates evidence you'll need for reporting to platforms or authorities. Engaging with the harasser often makes things worse."
        },
        {
            "question": "What is cyberstalking?",
            "options": [
                "Following someone on social media",
                "Persistent unwanted monitoring and contact that makes someone feel unsafe",
                "Looking at someone's public profile",
                "Disagreeing with someone online"
            ],
            "correct_answer": 1,
            "explanation": "Cyberstalking is persistent, unwanted monitoring and contact that goes beyond normal social media use and makes the target feel unsafe. It's a serious form of harassment that can escalate to physical stalking."
        },
        {
            "question": "Is online harassment ever the victim's fault?",
            "options": [
                "Yes, if they posted something controversial",
                "Yes, if they didn't use privacy settings",
                "No, the responsibility always lies with the harasser",
                "It depends on what they posted"
            ],
            "correct_answer": 2,
            "explanation": "Harassment is never the victim's fault, regardless of what they posted or their privacy settings. The responsibility for harassment always lies with the person doing the harassing."
        },
        {
            "question": "If a friend tells you they're being harassed online, what should you do first?",
            "options": [
                "Ask them what they did to cause it",
                "Confront the harasser yourself",
                "Believe them and offer support",
                "Tell them to ignore it"
            ],
            "correct_answer": 2,
            "explanation": "The most important thing is to believe your friend and offer support. Listen without judgment, respect their decisions, and help them access resources if needed. Never blame them or engage with the harasser."
        },
        {
            "question": "Why is it usually better not to respond to online harassers?",
            "options": [
                "Because they'll feel bad and stop",
                "Because any response often encourages them to continue or escalate",
                "Because it's rude to ignore people",
                "Because blocking is easier"
            ],
            "correct_answer": 1,
            "explanation": "Harassers often want any reaction, even a negative one. Responding typically encourages them to continue or escalate their behavior. The best approach is usually to document, block, and report without engaging."
        }
    ]
    lesson2.save()
    print(f"✓ Updated Lesson 2: {lesson2.title}")

    
    # Lesson 3: Securing Your Social Media
    lesson3 = Lesson.objects.get(id=3)
    lesson3.content = {
        "sections": [
            {
                "title": "The Social Media Security Challenge",
                "paragraphs": [
                    "Social media has woven itself into the fabric of daily life. We use it to stay connected with friends and family, share moments that matter to us, follow news and trends, and express ourselves. But every post, like, comment, and share creates data that platforms collect, analyze, and often monetize. Understanding how to secure your social media presence isn't about giving up these platforms entirely. It's about using them more safely and intentionally.",
                    "The challenge with social media security is that platforms profit from your engagement and data. Their default settings often prioritize data collection and sharing over your privacy. Features that seem convenient, like location tagging or facial recognition, can expose more information than you realize. The platforms themselves face constant security threats, with data breaches affecting millions of users.",
                    "Your social media accounts contain a wealth of personal information. They reveal your relationships, interests, opinions, location history, and daily patterns. In the wrong hands, this information can be used for identity theft, targeted scams, stalking, or reputation damage. Securing these accounts protects not just your data, but your safety, privacy, and peace of mind."
                ]
            },
            {
                "title": "The Foundation: Password Security",
                "paragraphs": [
                    "Your password is the primary barrier between your account and anyone who wants unauthorized access. Yet password security remains one of the most commonly overlooked aspects of online safety. Many people use passwords that are easy to remember, which unfortunately also makes them easy to guess or crack.",
                    "A strong password needs length and complexity. Aim for at least twelve characters, combining uppercase and lowercase letters, numbers, and symbols. Avoid using personal information like birthdays, names of family members, or common words. Hackers use sophisticated tools that can quickly crack simple passwords by trying millions of combinations.",
                    "The bigger challenge is using unique passwords for every account. When you reuse passwords, a breach at one service compromises all your accounts using that password. This is exactly what hackers count on. They obtain passwords from breached databases and try them across multiple platforms, a technique called credential stuffing.",
                    "Password managers solve the problem of creating and remembering unique, complex passwords. These tools generate random passwords for each account and store them securely, encrypted behind one master password. You only need to remember that single master password, while the manager handles everything else. This makes it practical to have truly strong, unique passwords everywhere.",
                    "Change your passwords periodically, especially after hearing about data breaches at services you use. If you've been using the same passwords for years, now is the time to update them. Start with your most important accounts like email, banking, and social media, then work through the rest."
                ]
            },
            {
                "title": "Adding a Second Layer of Protection",
                "paragraphs": [
                    "Two-factor authentication, often abbreviated as 2FA, adds a crucial second step to logging into your accounts. After entering your password, you need to provide a second form of verification. This might be a code sent to your phone, generated by an authentication app, or confirmed through a biometric scan like your fingerprint.",
                    "The security benefit is substantial. Even if someone discovers your password through a data breach, phishing attack, or by watching you type, they still can't access your account without that second factor. This single feature prevents the vast majority of unauthorized account access attempts.",
                    "Different types of 2FA offer varying levels of security. Text message codes are better than nothing but can be intercepted. Authentication apps like Google Authenticator or Authy are more secure, generating time-based codes that change every thirty seconds. Hardware security keys, physical devices you plug into your computer or tap on your phone, offer the highest security but require carrying the device with you.",
                    "Enable 2FA on every social media account that offers it. Yes, it adds an extra step when logging in. That minor inconvenience is worth the significant security improvement. Most platforms remember trusted devices, so you won't need to enter a code every single time, only when logging in from a new device or location.",
                    "Keep backup codes in a safe place. When you enable 2FA, platforms typically provide backup codes you can use if you lose access to your phone or authentication device. Store these codes securely, perhaps in a password manager or written down in a safe location. Without them, losing your phone could mean losing access to your accounts."
                ]
            },
            {
                "title": "Mastering Privacy Settings",
                "paragraphs": [
                    "Privacy settings control who can see your content, contact you, and find information about you. Unfortunately, most platforms set these to be quite open by default, encouraging maximum sharing and engagement. Taking control of these settings is essential for protecting your privacy.",
                    "Start with your profile visibility. Decide whether you want your account to be public or private. A private account means only approved followers can see your posts, while a public account is visible to anyone. There's no universally right choice, but consider who you want to reach and what you're comfortable sharing publicly.",
                    "Control who can contact you. Most platforms let you restrict who can send you messages, comment on your posts, or tag you in photos. You might allow messages only from people you follow, require approval for tags, or limit comments to friends. These settings help prevent unwanted contact and harassment.",
                    "Review what information appears on your profile. Your email address, phone number, birthday, and location don't need to be public. Hide this information or limit it to friends only. Remember that even information visible only to friends can be shared or screenshotted.",
                    "Location settings deserve special attention. Many platforms tag your location automatically when you post. Disable this feature. Sharing your location in real-time tells people where you are right now, which also means they know you're not home. If you want to share where you've been, do it after you've left.",
                    "Check your activity visibility settings. Platforms often show when you're online, when you've read messages, or what you've liked and commented on. You can usually hide this activity. Decide how much of your online behavior you want to be visible to others.",
                    "Review these settings regularly. Platforms frequently update their privacy options, sometimes resetting your preferences or adding new features with default settings that share more than you'd like. A quarterly privacy checkup helps ensure your settings still reflect your preferences."
                ]
            },
            {
                "title": "Thinking Before You Share",
                "paragraphs": [
                    "The most important security measure is also the simplest: think carefully before posting. Once something is online, you lose control over it. Even if you delete a post, it might have been screenshotted, shared, or archived. Approach every post with the assumption that it could become permanent and public.",
                    "Consider what your posts reveal about you. A photo might show your address in the background. A post about vacation plans announces that your home will be empty. A check-in at your gym reveals your routine. Individually, these might seem harmless, but together they create a detailed picture of your life that could be exploited.",
                    "Be especially cautious with personal information. Never post your full address, phone number, financial information, or identification documents. Be careful about sharing information that could be used to answer security questions, like your mother's maiden name or the street you grew up on.",
                    "Think about the long-term implications of what you share. Future employers might see your posts. Family members might come across content you'd rather they didn't see. What seems funny or appropriate now might not age well. When in doubt, don't post it.",
                    "Photos require particular care. Check backgrounds for identifying information like street signs, house numbers, or mail with your address visible. Consider whether you're comfortable with facial recognition technology identifying you in photos. Remember that photo metadata can include location information even if you don't explicitly tag your location.",
                    "If you share content about children, whether your own or others', be extremely cautious. Children can't consent to having their images and information shared online. Consider the digital footprint you're creating for them and whether they'd want this information public when they're older."
                ]
            },
            {
                "title": "Recognizing and Avoiding Social Media Scams",
                "paragraphs": [
                    "Social media platforms have become prime hunting grounds for scammers. The combination of personal information, trust between connections, and the casual nature of social media creates opportunities for fraud. Learning to recognize scams protects both you and your connections.",
                    "Phishing attempts on social media often impersonate the platform itself. You might receive a message claiming your account will be deleted unless you verify your information, or that you've violated community standards and need to appeal. These messages create urgency to make you act without thinking. Legitimate platforms don't ask for your password or personal information through direct messages.",
                    "Fake giveaways and contests are everywhere. They promise prizes for liking, sharing, and providing personal information. Real giveaways exist, but be skeptical. Check if the account is verified, research the company, and never provide sensitive information like your social security number or bank details to enter a contest.",
                    "Romance scams have moved to social media. Scammers create fake profiles, often using stolen photos, and build relationships with targets. After establishing trust, they ask for money, often with elaborate stories about emergencies or travel problems. Be wary of anyone you haven't met in person who asks for financial help, no matter how compelling their story.",
                    "Investment and money-making schemes promise unrealistic returns. Whether it's cryptocurrency, forex trading, or work-from-home opportunities, if it sounds too good to be true, it probably is. Legitimate investment opportunities don't come through unsolicited social media messages.",
                    "Account impersonation is common. Scammers clone profiles of your friends or family members and message you asking for money or personal information. If someone you know makes an unusual request, verify it through another channel before responding. Call them or send a message through a different platform.",
                    "Malicious links can install malware, steal your credentials, or take you to fake websites designed to look legitimate. Don't click links from people you don't know. Even links from friends should be approached cautiously, as their account might be compromised. Hover over links to see the actual URL before clicking."
                ]
            },
            {
                "title": "Managing Third-Party Access",
                "paragraphs": [
                    "Many apps and services request access to your social media accounts. You might use them to create content, analyze your followers, or play games. Each connection grants that third party access to some of your data. Over time, you accumulate numerous connected apps, many of which you no longer use.",
                    "Review your connected apps regularly. Every major platform has a section in settings showing which third-party apps have access to your account. Go through this list and remove anything you don't recognize or no longer use. Even apps you do use might have more access than necessary.",
                    "Before connecting a new app, read what permissions it's requesting. Does a photo editing app really need access to your friend list? Does a quiz need permission to post on your behalf? Be selective about what you allow. Many apps will still work with limited permissions.",
                    "Be particularly cautious with apps that request permission to post on your behalf. While convenient for scheduling posts or sharing content, this permission can be abused. If an app's security is compromised, hackers could use it to post spam or malicious content from your account.",
                    "Stick to official app stores when downloading applications. Third-party app stores and websites might offer modified versions of apps that contain malware. The official stores aren't perfect, but they provide some level of security screening.",
                    "Remember that data breaches don't just happen to social media platforms themselves. Third-party apps with access to your account can be breached too. When you hear about a breach affecting an app you've connected to your social media, change your passwords and review what data might have been exposed."
                ]
            },
            {
                "title": "Platform-Specific Security Measures",
                "paragraphs": [
                    "Each social media platform has unique security features and vulnerabilities. Understanding the specific tools available on the platforms you use most helps you secure them effectively.",
                    "Facebook offers extensive privacy controls. Use the 'View As' feature to see what your profile looks like to the public or specific friends. Review your timeline and tagging settings to control who can post on your timeline and whether you need to approve tags. Check your face recognition settings and decide whether you want Facebook to identify you in photos. Review your ad preferences to limit how your data is used for advertising.",
                    "Instagram's privacy settings are simpler but important. Making your account private means only approved followers see your posts. The 'Restrict' feature lets you limit someone's interactions without blocking them, useful for handling uncomfortable situations subtly. Control who can comment on your posts, send you messages, and see your story. Review which accounts can tag you in posts and stories.",
                    "Twitter's privacy options include protecting your tweets, which makes your account private. Control who can tag you in photos and whether your location is added to tweets. Mute keywords, phrases, and accounts to filter your experience without blocking. Regularly review which apps have access to your Twitter account, as this platform is particularly popular for third-party integrations.",
                    "TikTok collects extensive data, so privacy settings are crucial. Make your account private to control who can see your videos. Decide who can comment, duet, or stitch your videos. Disable location services for the app. Review your privacy settings to limit data collection where possible. Be aware that TikTok's data practices have raised security concerns, so consider what you're comfortable sharing on the platform.",
                    "LinkedIn requires a different approach since it's professional. Control your profile visibility and who can see your connections. Turn off activity broadcasts if you don't want your network notified every time you update your profile. Manage who can see your email address and phone number. Be cautious about connection requests from people you don't know professionally."
                ]
            },
            {
                "title": "Maintaining Your Digital Reputation",
                "paragraphs": [
                    "Your social media presence creates a digital reputation that can affect your personal and professional life. Employers, colleagues, potential romantic partners, and others can find your profiles and form impressions based on what they see. Managing this reputation is part of social media security.",
                    "Google yourself regularly to see what information about you is publicly available. Search for your name, username, and any variations. Check both regular search and image search. This shows you what others can easily find about you and helps you identify information you might want to remove or make private.",
                    "Old accounts you no longer use can be security vulnerabilities and reputation risks. They might have outdated information, weak passwords, or content that no longer represents you. Take time to find and delete these accounts. If you can't delete them, at least secure them with strong passwords and private settings.",
                    "Review your post history periodically. What you posted years ago might not reflect who you are now. Many platforms let you bulk delete old posts or limit who can see them. Consider whether old posts could be misinterpreted or cause problems. It's okay to curate your online presence.",
                    "Remember that comments on others' posts are part of your digital footprint too. What you say in comment sections is often public and searchable. Approach commenting with the same thoughtfulness you'd apply to your own posts.",
                    "Consider maintaining separate accounts for personal and professional use. This lets you share more freely with friends while keeping your professional image polished. Just be sure to secure both accounts properly and be mindful of which account you're using when posting."
                ]
            },
            {
                "title": "Staying Secure in an Evolving Landscape",
                "paragraphs": [
                    "Social media security isn't a one-time task but an ongoing practice. Platforms change, new threats emerge, and your own needs and comfort levels evolve. Staying secure requires staying informed and adapting your practices accordingly.",
                    "Follow security news related to the platforms you use. When a platform announces a data breach or security vulnerability, take recommended actions promptly. Change your password, review your account for suspicious activity, and check what information might have been exposed.",
                    "Enable security notifications on all your accounts. These alerts tell you about login attempts from new devices, password changes, and other account activity. If you receive a notification about activity you didn't initiate, act immediately to secure your account.",
                    "Keep your apps updated. Updates often include security patches that fix vulnerabilities. Enable automatic updates when possible, or at least update promptly when notified. This applies to both the social media apps themselves and your device's operating system.",
                    "Learn about new security features as platforms introduce them. Companies do occasionally add better privacy controls or security options. When you hear about a new feature, take a few minutes to understand it and decide whether to enable it.",
                    "Share what you learn with friends and family. Social media security affects everyone, and many people don't know how to protect themselves. When you discover a useful security tip or privacy setting, pass it along. Creating a more security-conscious community benefits everyone.",
                    "Remember that security and convenience often involve tradeoffs. More security might mean more steps to log in or less seamless sharing. Decide what balance works for you. Perfect security isn't realistic, but better security is always achievable. Every step you take to protect your accounts makes you safer online and helps you use social media with greater confidence and peace of mind."
                ]
            }
        ]
    }
    lesson3.quiz = [
        {
            "question": "Why is it important to use unique passwords for each social media account?",
            "options": [
                "To make them harder to remember",
                "So that a breach at one service doesn't compromise all your accounts",
                "Because platforms require it",
                "To confuse hackers"
            ],
            "correct_answer": 1,
            "explanation": "Using unique passwords means that if one service is breached, your other accounts remain secure. This is one of the most effective ways to protect yourself, as hackers often try stolen passwords across multiple platforms."
        },
        {
            "question": "What is the main security benefit of two-factor authentication?",
            "options": [
                "It makes logging in faster",
                "It eliminates the need for passwords",
                "It requires a second verification step beyond your password",
                "It automatically backs up your account"
            ],
            "correct_answer": 2,
            "explanation": "Two-factor authentication adds a second layer of security. Even if someone gets your password, they can't access your account without the second factor, typically a code sent to your phone or generated by an app."
        },
        {
            "question": "When is it safest to share your location on social media?",
            "options": [
                "In real-time so friends know where you are",
                "After you've left the location",
                "Only during daytime",
                "Location sharing is always safe"
            ],
            "correct_answer": 1,
            "explanation": "Sharing your location after you've left is safer because it doesn't tell people where you are right now or that your home is empty. Real-time location sharing can create safety risks."
        },
        {
            "question": "What should you do with third-party apps connected to your social media?",
            "options": [
                "Connect as many as possible",
                "Never review them",
                "Regularly review and remove apps you don't use",
                "Give them all full access"
            ],
            "correct_answer": 2,
            "explanation": "You should regularly review connected apps and remove any you no longer use or trust. Each connected app has access to some of your data, and many data breaches happen through third-party apps rather than the main platform."
        },
        {
            "question": "Why should you Google yourself regularly?",
            "options": [
                "To boost your ego",
                "To see what information about you is publicly available",
                "To improve your search ranking",
                "To find old friends"
            ],
            "correct_answer": 1,
            "explanation": "Googling yourself shows you what information about you is publicly available and what others can easily find. This helps you identify information you might want to remove or make private to protect your digital reputation."
        }
    ]
    lesson3.save()
    print(f"✓ Updated Lesson 3: {lesson3.title}")
    
    print("\n✅ All lessons updated with natural editorial content!")
    print("\nLesson Summary:")
    for lesson in Lesson.objects.all().order_by('id'):
        print(f"\n{lesson.id}. {lesson.title}")
        print(f"   Category: {lesson.category} | Difficulty: {lesson.difficulty}")
        print(f"   Duration: {lesson.duration_minutes} minutes")
        print(f"   Sections: {len(lesson.content.get('sections', []))}")
        print(f"   Quiz questions: {len(lesson.quiz)}")


if __name__ == '__main__':
    update_lessons()
