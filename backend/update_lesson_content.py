"""
Update lessons with comprehensive educational content.
This script populates all lessons with full LMS-style content.
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
django.setup()

from apps.lessons.models import Lesson


def update_lessons():
    """Update all lessons with comprehensive content"""
    
    # Lesson 1: Understanding Digital Privacy
    lesson1 = Lesson.objects.get(id=1)
    lesson1.content = {
        "sections": [
            {
                "title": "Introduction to Digital Privacy",
                "text": "Digital privacy is about controlling who has access to your personal information online. In today's connected world, every click, search, and interaction leaves a digital footprint. Understanding how to protect your privacy is essential for your safety and security."
            },
            {
                "title": "What is Personal Information?",
                "text": "Personal information includes your name, address, phone number, email, date of birth, photos, location data, browsing history, and even your preferences and habits. This information can be used to identify you, track your activities, or even steal your identity."
            },
            {
                "title": "Why Privacy Matters",
                "text": "Your privacy matters because:\n\n• Identity theft: Criminals can use your information to impersonate you\n• Financial fraud: Access to your data can lead to unauthorized transactions\n• Personal safety: Location data and personal details can put you at physical risk\n• Reputation: Private information shared publicly can damage your reputation\n• Autonomy: You have the right to control your own information"
            },
            {
                "title": "Common Privacy Risks",
                "text": "Be aware of these common privacy threats:\n\n• Social media oversharing: Posting too much personal information publicly\n• Weak passwords: Easy-to-guess passwords that give hackers access\n• Public Wi-Fi: Unsecured networks that can intercept your data\n• Phishing: Fake emails or messages trying to steal your information\n• Data breaches: Companies losing your data to hackers\n• Tracking cookies: Websites following your online behavior"
            },
            {
                "title": "Privacy Protection Basics",
                "text": "Start protecting your privacy with these essential steps:\n\n1. Use strong, unique passwords for each account\n2. Enable two-factor authentication (2FA) wherever possible\n3. Review and adjust privacy settings on all social media accounts\n4. Be cautious about what you share online\n5. Use a VPN when on public Wi-Fi\n6. Regularly update your software and apps\n7. Read privacy policies before accepting them\n8. Use privacy-focused browsers and search engines"
            },
            {
                "title": "Social Media Privacy",
                "text": "Social media platforms collect extensive data about you. Protect yourself by:\n\n• Setting your profiles to private\n• Limiting who can see your posts and personal information\n• Being selective about friend/follower requests\n• Avoiding posting your location in real-time\n• Not sharing sensitive information like your address or phone number\n• Reviewing tagged photos before they appear on your profile\n• Regularly auditing your privacy settings"
            },
            {
                "title": "Mobile Device Privacy",
                "text": "Your smartphone knows a lot about you. Secure it by:\n\n• Using a strong passcode or biometric lock\n• Reviewing app permissions regularly\n• Only downloading apps from official stores\n• Disabling location services for apps that don't need it\n• Keeping your operating system updated\n• Being careful with public charging stations\n• Encrypting your device"
            },
            {
                "title": "Online Shopping and Banking",
                "text": "When handling financial transactions online:\n\n• Only use secure websites (look for HTTPS and the padlock icon)\n• Never save payment information on websites\n• Use virtual credit cards when possible\n• Monitor your accounts regularly for suspicious activity\n• Avoid shopping on public Wi-Fi\n• Be wary of deals that seem too good to be true\n• Use strong, unique passwords for financial accounts"
            },
            {
                "title": "Email Privacy",
                "text": "Email is a common target for privacy breaches. Protect your email by:\n\n• Using a secure email provider\n• Never clicking suspicious links or attachments\n• Being cautious about what you write in emails\n• Using encryption for sensitive communications\n• Creating separate email addresses for different purposes\n• Regularly cleaning out old emails\n• Enabling spam filters"
            },
            {
                "title": "Taking Action Today",
                "text": "Start improving your digital privacy right now:\n\n1. Change any weak or reused passwords\n2. Enable 2FA on your most important accounts\n3. Review privacy settings on your top 3 social media platforms\n4. Delete apps you no longer use\n5. Clear your browser cookies and cache\n6. Set up a password manager\n7. Review what information about you is publicly available online\n\nRemember: Privacy is not about having something to hide—it's about having something to protect. Your personal information, safety, and autonomy are worth protecting."
            }
        ]
    }
    lesson1.quiz = [
        {
            "question": "What is digital privacy?",
            "options": [
                "Keeping your computer private",
                "Controlling who has access to your personal information online",
                "Using private browsing mode",
                "Not using social media"
            ],
            "correct_answer": 1,
            "explanation": "Digital privacy is about controlling who has access to your personal information online, including your data, activities, and identity."
        },
        {
            "question": "Which of these is NOT considered personal information?",
            "options": [
                "Your browsing history",
                "Your location data",
                "Public news articles",
                "Your email address"
            ],
            "correct_answer": 2,
            "explanation": "Public news articles are not personal information. Your browsing history, location data, and email address are all personal information that can identify you."
        },
        {
            "question": "What is two-factor authentication (2FA)?",
            "options": [
                "Using two passwords",
                "An extra security step requiring a second form of verification",
                "Having two email accounts",
                "Logging in twice"
            ],
            "correct_answer": 1,
            "explanation": "Two-factor authentication adds an extra layer of security by requiring a second form of verification (like a code sent to your phone) in addition to your password."
        },
        {
            "question": "When is it safe to use public Wi-Fi for sensitive activities?",
            "options": [
                "Always, if it's free",
                "When using a VPN",
                "During daytime only",
                "Never, under any circumstances"
            ],
            "correct_answer": 1,
            "explanation": "Public Wi-Fi can be made safer by using a VPN (Virtual Private Network), which encrypts your data. However, it's still best to avoid highly sensitive activities on public networks."
        },
        {
            "question": "What should you do if you receive a suspicious email asking for personal information?",
            "options": [
                "Reply with the information requested",
                "Click the link to verify it's legitimate",
                "Delete it and report it as phishing",
                "Forward it to all your contacts"
            ],
            "correct_answer": 2,
            "explanation": "Suspicious emails asking for personal information are likely phishing attempts. Delete them and report them. Never click links or provide information."
        }
    ]
    lesson1.save()
    print(f"✓ Updated Lesson 1: {lesson1.title}")
    
    # Lesson 2: Recognizing Online Harassment
    lesson2 = Lesson.objects.get(id=2)
    lesson2.content = {
        "sections": [
            {
                "title": "Understanding Online Harassment",
                "text": "Online harassment, also known as cyberbullying or digital abuse, is the use of technology to harass, threaten, embarrass, or target another person. It can happen through social media, messaging apps, emails, gaming platforms, or any digital communication channel. Understanding what constitutes harassment is the first step in protecting yourself and others."
            },
            {
                "title": "Types of Online Harassment",
                "text": "Online harassment takes many forms:\n\n• Cyberbullying: Repeated hostile behavior intended to harm or intimidate\n• Cyberstalking: Persistent unwanted contact and monitoring\n• Doxing: Publishing private information without consent\n• Impersonation: Creating fake accounts pretending to be you\n• Harassment campaigns: Coordinated attacks by multiple people\n• Revenge porn: Sharing intimate images without consent\n• Trolling: Deliberately provocative or offensive comments\n• Threats: Direct threats of violence or harm\n• Hate speech: Attacks based on identity (gender, race, religion, etc.)"
            },
            {
                "title": "Warning Signs of Harassment",
                "text": "Recognize these red flags:\n\n• Receiving repeated unwanted messages or comments\n• Someone monitoring your online activities\n• Threatening or intimidating messages\n• Spreading rumors or false information about you\n• Sharing your private information publicly\n• Creating fake profiles using your name or photos\n• Persistent contact after you've asked them to stop\n• Comments that make you feel unsafe or uncomfortable\n• Coordinated negative attention from multiple accounts"
            },
            {
                "title": "The Impact of Online Harassment",
                "text": "Online harassment can have serious effects:\n\n• Emotional distress: Anxiety, depression, fear, and stress\n• Physical symptoms: Sleep problems, headaches, loss of appetite\n• Social isolation: Withdrawing from online and offline activities\n• Professional consequences: Damage to reputation or career\n• Safety concerns: Fear for personal safety\n• Loss of confidence: Reduced self-esteem and trust in others\n\nRemember: The impact is real, even if the harassment is online. Your feelings are valid, and you deserve support."
            },
            {
                "title": "Immediate Safety Steps",
                "text": "If you're experiencing harassment right now:\n\n1. Don't engage: Don't respond to the harasser—it often escalates the situation\n2. Document everything: Take screenshots with dates and times\n3. Block the harasser: Use platform blocking features\n4. Report to the platform: Use reporting tools on social media and apps\n5. Adjust privacy settings: Limit who can contact you or see your content\n6. Tell someone you trust: Don't face this alone\n7. Consider taking a break: It's okay to step away from social media\n8. Secure your accounts: Change passwords and enable 2FA"
            },
            {
                "title": "Documentation and Evidence",
                "text": "Proper documentation is crucial:\n\n• Take screenshots of all harassing messages, posts, and profiles\n• Include dates, times, and usernames\n• Save URLs and links\n• Keep a written log of incidents\n• Don't delete original messages (even if upsetting)\n• Store evidence in a safe place\n• Consider using screen recording for ongoing harassment\n• Document any offline incidents related to online harassment\n\nThis evidence may be needed for reporting to platforms, employers, schools, or law enforcement."
            },
            {
                "title": "Reporting and Getting Help",
                "text": "Take action by reporting harassment:\n\n• Platform reporting: Use built-in reporting tools on social media and apps\n• School or workplace: Report to appropriate authorities if relevant\n• Law enforcement: Contact police for threats, stalking, or illegal content\n• Support organizations: Reach out to anti-harassment organizations\n• Legal advice: Consult a lawyer for serious cases\n• Mental health support: Talk to a counselor or therapist\n\nYou don't have to handle this alone. There are people and organizations ready to help."
            },
            {
                "title": "Platform-Specific Actions",
                "text": "Most platforms have tools to combat harassment:\n\n• Block and mute: Prevent harassers from contacting you\n• Report abuse: Flag content that violates platform policies\n• Restrict comments: Limit who can comment on your posts\n• Filter messages: Automatically filter messages from non-followers\n• Hide your online status: Don't let harassers know when you're active\n• Limit tagging: Control who can tag you in posts\n• Review followers: Remove suspicious or fake accounts\n• Make accounts private: Control who can see your content"
            },
            {
                "title": "Supporting Others",
                "text": "If someone you know is being harassed:\n\n• Believe them: Take their experience seriously\n• Listen without judgment: Let them share at their own pace\n• Don't blame them: Harassment is never the victim's fault\n• Offer practical help: Assist with documentation or reporting\n• Respect their decisions: Let them choose how to respond\n• Check in regularly: Ongoing support matters\n• Don't engage with the harasser: This can make things worse\n• Connect them with resources: Share information about support services\n• Be patient: Recovery takes time"
            },
            {
                "title": "Prevention and Protection",
                "text": "Reduce your risk of harassment:\n\n• Use strong privacy settings on all platforms\n• Be selective about what you share publicly\n• Think before posting: Consider how content might be misused\n• Use separate accounts for personal and professional life\n• Be cautious about accepting friend/follow requests\n• Don't share your location in real-time\n• Use pseudonyms when appropriate\n• Regularly review your digital footprint\n• Trust your instincts: If something feels wrong, it probably is\n\nRemember: Taking precautions doesn't mean you're responsible if harassment occurs. The responsibility always lies with the harasser."
            },
            {
                "title": "Legal Rights and Options",
                "text": "You have legal protections:\n\n• Many forms of online harassment are illegal\n• Laws vary by location but may cover stalking, threats, defamation, and more\n• You can pursue civil or criminal action\n• Restraining orders may be available\n• Some platforms must comply with legal requests to remove content\n• Document everything for potential legal action\n• Consult with a lawyer familiar with cyber harassment\n• Know your rights under platform terms of service\n\nDon't hesitate to explore legal options if harassment is severe or persistent."
            },
            {
                "title": "Moving Forward",
                "text": "Recovering from online harassment:\n\n• Prioritize self-care: Take care of your mental and physical health\n• Rebuild your online presence: Reclaim your digital space on your terms\n• Set boundaries: Decide what level of online engagement feels safe\n• Connect with supportive communities: Find positive online spaces\n• Consider professional help: Therapy can help process the experience\n• Advocate for change: Share your story if you feel comfortable\n• Remember it's not your fault: You deserve to be online without harassment\n\nYou are not alone. Many people have experienced online harassment and have found ways to heal and thrive. Your safety and well-being matter."
            }
        ]
    }
    lesson2.quiz = [
        {
            "question": "What is cyberstalking?",
            "options": [
                "Looking at someone's public social media profile",
                "Persistent unwanted contact and monitoring online",
                "Following someone on social media",
                "Reading someone's blog"
            ],
            "correct_answer": 1,
            "explanation": "Cyberstalking is persistent, unwanted contact and monitoring that makes someone feel unsafe. It goes beyond normal social media use and involves harassment."
        },
        {
            "question": "What should you do FIRST if you're being harassed online?",
            "options": [
                "Respond to the harasser to tell them to stop",
                "Delete all your social media accounts",
                "Document the harassment with screenshots",
                "Post about it publicly"
            ],
            "correct_answer": 2,
            "explanation": "The first step is to document everything with screenshots, dates, and times. This evidence is crucial for reporting and potential legal action."
        },
        {
            "question": "Is it ever the victim's fault if they experience online harassment?",
            "options": [
                "Yes, if they posted something controversial",
                "Yes, if they didn't use privacy settings",
                "No, harassment is always the harasser's responsibility",
                "It depends on the situation"
            ],
            "correct_answer": 2,
            "explanation": "Harassment is NEVER the victim's fault. The responsibility always lies with the person doing the harassing, regardless of circumstances."
        },
        {
            "question": "What is 'doxing'?",
            "options": [
                "Blocking someone online",
                "Publishing someone's private information without consent",
                "Creating a fake profile",
                "Reporting harassment to authorities"
            ],
            "correct_answer": 1,
            "explanation": "Doxing is the malicious act of publishing someone's private information (like address, phone number, or workplace) without their consent, often to intimidate or harm them."
        },
        {
            "question": "If a friend tells you they're being harassed online, what should you do?",
            "options": [
                "Tell them to ignore it",
                "Confront the harasser yourself",
                "Believe them and offer support",
                "Ask them what they did to cause it"
            ],
            "correct_answer": 2,
            "explanation": "The most important thing is to believe your friend and offer support. Listen without judgment, respect their decisions, and help them access resources if needed."
        }
    ]
    lesson2.save()
    print(f"✓ Updated Lesson 2: {lesson2.title}")
    
    # Lesson 3: Securing Your Social Media
    lesson3 = Lesson.objects.get(id=3)
    lesson3.content = {
        "sections": [
            {
                "title": "Introduction to Social Media Security",
                "text": "Social media platforms have become central to how we communicate, share, and connect. However, they also collect vast amounts of personal data and can expose you to various security risks. Learning to secure your social media accounts is essential for protecting your privacy, identity, and personal safety in the digital age."
            },
            {
                "title": "Understanding Social Media Risks",
                "text": "Social media platforms present several security challenges:\n\n• Data collection: Platforms track your behavior, preferences, and connections\n• Account hijacking: Hackers can take over your accounts\n• Identity theft: Personal information can be used to impersonate you\n• Phishing attacks: Fake messages trying to steal your credentials\n• Malware: Malicious links that infect your device\n• Social engineering: Manipulating you into revealing information\n• Privacy breaches: Your data being shared or sold without consent\n• Reputation damage: Content affecting your personal or professional life\n• Location tracking: Real-time location data putting you at risk"
            },
            {
                "title": "Strong Password Practices",
                "text": "Your password is your first line of defense:\n\n• Use unique passwords for each platform (never reuse passwords)\n• Create strong passwords: At least 12 characters with uppercase, lowercase, numbers, and symbols\n• Avoid personal information: Don't use birthdays, names, or common words\n• Use a password manager: Let it generate and store complex passwords\n• Change passwords regularly: Especially after security breaches\n• Never share passwords: Even with friends or family\n• Avoid password hints: They make it easier for hackers to guess\n• Use passphrases: Long phrases are easier to remember and harder to crack\n\nExample of a strong password: Tr0pic@l-Sunset-2024-Beach!"
            },
            {
                "title": "Two-Factor Authentication (2FA)",
                "text": "2FA adds a critical extra layer of security:\n\n• What it is: A second verification step beyond your password\n• How it works: After entering your password, you need a code from your phone or email\n• Types of 2FA:\n  - SMS codes (text messages)\n  - Authentication apps (Google Authenticator, Authy)\n  - Biometric verification (fingerprint, face recognition)\n  - Hardware keys (physical security devices)\n\n• Enable 2FA on ALL social media accounts\n• Use authentication apps instead of SMS when possible (more secure)\n• Keep backup codes in a safe place\n• Update your phone number if it changes\n\nWith 2FA enabled, even if someone gets your password, they can't access your account without the second factor."
            },
            {
                "title": "Privacy Settings Mastery",
                "text": "Take control of your privacy settings:\n\n• Profile visibility: Set accounts to private or friends-only\n• Post audience: Control who can see each post\n• Tagging: Require approval before appearing in tagged photos\n• Search visibility: Limit who can find you via search\n• Contact information: Hide email and phone number\n• Location services: Disable location tagging\n• Activity status: Hide when you're online\n• Story settings: Control who sees your stories\n• App permissions: Review what third-party apps can access\n• Ad preferences: Limit data used for advertising\n\nReview these settings regularly—platforms often change their privacy options."
            },
            {
                "title": "Platform-Specific Security",
                "text": "Each platform has unique security features:\n\n**Facebook:**\n• Use 'View As' to see what others see on your profile\n• Review login alerts for suspicious activity\n• Limit past posts visibility\n• Control who can send you friend requests\n\n**Instagram:**\n• Make your account private\n• Restrict accounts without blocking them\n• Control who can comment and message you\n• Hide your story from specific people\n\n**Twitter/X:**\n• Protect your tweets (make account private)\n• Control who can tag you in photos\n• Mute keywords and accounts\n• Review connected apps regularly\n\n**TikTok:**\n• Set account to private\n• Control who can duet, stitch, or comment\n• Disable location services\n• Limit data collection in privacy settings\n\n**LinkedIn:**\n• Control profile visibility\n• Manage who can see your connections\n• Turn off activity broadcasts\n• Review profile viewers settings"
            },
            {
                "title": "Safe Sharing Practices",
                "text": "Think before you post:\n\n• Personal information: Never share your address, phone number, or financial details\n• Location: Don't post your location in real-time (wait until you've left)\n• Travel plans: Don't announce when your home will be empty\n• Photos: Check backgrounds for identifying information\n• Children: Be extremely cautious about sharing children's photos or information\n• Work information: Don't share sensitive work details\n• Routine: Avoid posting patterns that reveal your schedule\n• Emotions: Be careful posting when angry or upset\n• Permanent nature: Remember that screenshots exist forever\n\nAsk yourself: 'Would I be comfortable with a stranger knowing this?'"
            },
            {
                "title": "Recognizing and Avoiding Scams",
                "text": "Social media is full of scams. Watch out for:\n\n• Phishing messages: Fake messages claiming to be from the platform\n• Fake giveaways: 'You've won!' messages requiring personal information\n• Romance scams: Fake profiles building relationships to steal money\n• Investment scams: Too-good-to-be-true financial opportunities\n• Impersonation: Fake accounts pretending to be friends or celebrities\n• Malicious links: Links that install malware or steal credentials\n• Fake verification: Messages claiming you need to verify your account\n\nRed flags:\n• Urgent language ('Act now!' 'Your account will be deleted!')\n• Requests for passwords or payment information\n• Poor grammar or spelling\n• Suspicious links or attachments\n• Offers that seem too good to be true\n\nWhen in doubt, verify directly with the platform or person through official channels."
            },
            {
                "title": "Managing Third-Party Apps",
                "text": "Third-party apps can access your social media data:\n\n• Review connected apps: Check what apps have access to your accounts\n• Revoke unnecessary access: Remove apps you no longer use\n• Check permissions: See what data each app can access\n• Be selective: Only connect apps you truly need and trust\n• Read permissions carefully: Before granting access, understand what you're allowing\n• Regular audits: Review connected apps every few months\n• Official apps only: Download apps from official stores\n\nMany data breaches happen through third-party apps, not the main platform."
            },
            {
                "title": "Account Recovery and Backup",
                "text": "Prepare for account issues:\n\n• Recovery email: Keep a current, secure recovery email address\n• Recovery phone: Maintain an up-to-date phone number\n• Backup codes: Save 2FA backup codes securely\n• Trusted contacts: Set up trusted friends for account recovery (where available)\n• Security questions: Use answers that aren't easily guessable\n• Regular backups: Download your data periodically\n• Document important content: Keep copies of important posts or messages\n\nIf your account is compromised:\n1. Try to change your password immediately\n2. Use account recovery options\n3. Report to the platform\n4. Warn your contacts about the compromise\n5. Check for unauthorized posts or messages\n6. Review account settings for changes"
            },
            {
                "title": "Digital Footprint Management",
                "text": "Your social media presence creates a digital footprint:\n\n• Google yourself: See what information is publicly available\n• Old accounts: Delete or secure accounts you no longer use\n• Past posts: Review and delete old posts that no longer represent you\n• Tagged content: Untag yourself from inappropriate content\n• Comments: Remember that comments on others' posts are visible\n• Professional image: Consider how your presence affects career opportunities\n• Separate accounts: Consider separate personal and professional accounts\n• Regular cleanup: Periodically review and clean up your content\n\nYour digital footprint can affect job opportunities, relationships, and personal safety."
            },
            {
                "title": "Staying Informed and Updated",
                "text": "Social media security is constantly evolving:\n\n• Follow platform security blogs: Stay updated on new features and threats\n• Enable security notifications: Get alerts about login attempts and changes\n• Update apps regularly: New versions often include security fixes\n• Learn about new scams: Stay informed about current threats\n• Review terms of service: Understand how your data is used\n• Join security communities: Learn from others' experiences\n• Educate others: Share security tips with friends and family\n• Stay skeptical: Question suspicious activity\n\nSecurity is an ongoing process, not a one-time setup."
            },
            {
                "title": "Taking Action Now",
                "text": "Secure your social media today:\n\n**Immediate actions (next 30 minutes):**\n1. Enable 2FA on all your social media accounts\n2. Change any weak or reused passwords\n3. Review privacy settings on your most-used platform\n4. Remove any suspicious third-party apps\n\n**This week:**\n5. Set all accounts to private or friends-only\n6. Review and clean up old posts\n7. Check who can see your contact information\n8. Set up a password manager\n\n**This month:**\n9. Review all privacy settings on every platform\n10. Delete unused social media accounts\n11. Audit your digital footprint\n12. Educate family members about social media security\n\nRemember: Your social media security directly impacts your real-world safety. Taking these steps protects not just your accounts, but your identity, reputation, and personal well-being. You deserve to use social media safely and confidently."
            }
        ]
    }
    lesson3.quiz = [
        {
            "question": "What makes a password strong?",
            "options": [
                "Using your birthday",
                "At least 12 characters with uppercase, lowercase, numbers, and symbols",
                "Using the same password everywhere",
                "Using common words"
            ],
            "correct_answer": 1,
            "explanation": "A strong password has at least 12 characters and includes a mix of uppercase letters, lowercase letters, numbers, and symbols. It should be unique and not based on personal information."
        },
        {
            "question": "What is the main benefit of two-factor authentication (2FA)?",
            "options": [
                "It makes logging in faster",
                "It eliminates the need for a password",
                "It adds an extra security layer beyond your password",
                "It automatically backs up your account"
            ],
            "correct_answer": 2,
            "explanation": "2FA adds an extra layer of security by requiring a second form of verification (like a code from your phone) in addition to your password, making it much harder for hackers to access your account."
        },
        {
            "question": "When is it safe to share your location on social media?",
            "options": [
                "In real-time, so friends know where you are",
                "After you've left the location",
                "Only on weekends",
                "Never, under any circumstances"
            ],
            "correct_answer": 1,
            "explanation": "It's safer to share your location after you've left, rather than in real-time. This prevents people from knowing your current whereabouts and reduces safety risks."
        },
        {
            "question": "What should you do with third-party apps connected to your social media?",
            "options": [
                "Connect as many as possible for convenience",
                "Never review them",
                "Regularly review and remove apps you don't use",
                "Share your password with them"
            ],
            "correct_answer": 2,
            "explanation": "You should regularly review connected third-party apps and remove any you no longer use or trust. Many data breaches happen through third-party apps."
        },
        {
            "question": "What is a 'digital footprint'?",
            "options": [
                "The size of your social media profile picture",
                "The trail of data you leave online through your activities",
                "Your shoe size posted online",
                "The number of followers you have"
            ],
            "correct_answer": 1,
            "explanation": "Your digital footprint is the trail of data and information you leave online through your posts, comments, likes, and other activities. It can affect your reputation and opportunities."
        }
    ]
    lesson3.save()
    print(f"✓ Updated Lesson 3: {lesson3.title}")
    
    print("\n✅ All lessons updated successfully with comprehensive content!")
    print("\nLesson Summary:")
    for lesson in Lesson.objects.all().order_by('id'):
        print(f"\n{lesson.id}. {lesson.title}")
        print(f"   Category: {lesson.category} | Difficulty: {lesson.difficulty}")
        print(f"   Duration: {lesson.duration_minutes} minutes")
        print(f"   Sections: {len(lesson.content.get('sections', []))}")
        print(f"   Quiz questions: {len(lesson.quiz)}")


if __name__ == '__main__':
    update_lessons()
