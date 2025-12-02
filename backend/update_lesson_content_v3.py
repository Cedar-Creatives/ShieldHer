"""
Update lessons with concise, actionable content.
Focus on quick insights and practical steps, not lengthy education.
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
django.setup()

from apps.lessons.models import Lesson


def update_lessons():
    """Update all lessons with concise, actionable content"""
    
    # Lesson 1: Understanding Digital Privacy
    lesson1 = Lesson.objects.get(id=1)
    lesson1.content = {
        "sections": [
            {
                "title": "Your Digital Footprint",
                "paragraphs": [
                    "Every time you go online, you leave traces. These traces can reveal where you are, who you talk to, and what you're doing. For someone in an unsafe situation, this information can be dangerous.",
                    "The good news? You can take control. Small changes to how you use technology can make a big difference in protecting yourself."
                ]
            },
            {
                "title": "What You Need to Know",
                "paragraphs": [
                    "Your phone and computer track more than you realize. Location services know where you've been. Browsing history shows what you've searched for. Social media reveals your connections and daily patterns.",
                    "If someone has access to your devices or accounts, they can see all of this. That's why protecting your digital privacy isn't just about security—it's about safety."
                ]
            },
            {
                "title": "Start Here: Three Essential Steps",
                "paragraphs": [
                    "First, use strong, unique passwords for each account. A password manager can help you create and remember them. This single step prevents one compromised account from affecting all your others.",
                    "Second, enable two-factor authentication wherever possible. Even if someone gets your password, they'll need your phone to access your account.",
                    "Third, review your privacy settings on social media. Make your accounts private, limit who can see your posts, and turn off location tagging."
                ]
            },
            {
                "title": "Social Media Safety",
                "paragraphs": [
                    "Think before you post. Photos can reveal your location through backgrounds or metadata. Posts about your routine tell people when you're home or away. Information that seems harmless alone can be dangerous when pieced together.",
                    "Set your accounts to private. Approve followers carefully. Don't share your location in real-time. These simple boundaries can significantly improve your safety."
                ]
            },
            {
                "title": "Your Phone, Your Privacy",
                "paragraphs": [
                    "Your phone knows everything about you. Protect it with a strong passcode or biometric lock. Review which apps have access to your location, contacts, and photos. Many apps don't need the permissions they ask for.",
                    "Be cautious with public charging stations—they can be used to access your data. If you must use one, consider a data blocker device or use your own charging cable with a wall adapter."
                ]
            },
            {
                "title": "Taking Action Today",
                "paragraphs": [
                    "You don't need to do everything at once. Start with one or two changes today. Change your most important passwords. Enable two-factor authentication on your email. Check your social media privacy settings.",
                    "Each small step makes you safer. Privacy isn't about perfection—it's about progress. You have the right to control your information and protect yourself online."
                ]
            }
        ]
    }
    lesson1.quiz = [
        {
            "question": "Why is digital privacy important for personal safety?",
            "options": [
                "It makes your computer run faster",
                "It prevents others from tracking your location and activities",
                "It's only important for celebrities",
                "It's not really necessary"
            ],
            "correct_answer": 1,
            "explanation": "Digital privacy is crucial for safety because it prevents others from tracking your location, monitoring your activities, and accessing personal information that could put you at risk."
        },
        {
            "question": "What's the most important first step in protecting your accounts?",
            "options": [
                "Deleting all social media",
                "Using strong, unique passwords for each account",
                "Never going online",
                "Buying expensive security software"
            ],
            "correct_answer": 1,
            "explanation": "Using strong, unique passwords for each account is the foundation of digital security. It ensures that if one account is compromised, your other accounts remain safe."
        },
        {
            "question": "When should you share your location on social media?",
            "options": [
                "In real-time so friends know where you are",
                "After you've left the location",
                "Always, it's perfectly safe",
                "Only on weekends"
            ],
            "correct_answer": 1,
            "explanation": "Share your location only after you've left. Real-time location sharing tells people exactly where you are right now, which can be dangerous."
        }
    ]
    lesson1.save()
    print(f"✓ Updated Lesson 1: {lesson1.title}")
    
    # Lesson 2: Recognizing Online Harassment
    lesson2 = Lesson.objects.get(id=2)
    lesson2.content = {
        "sections": [
            {
                "title": "What Online Harassment Looks Like",
                "paragraphs": [
                    "Online harassment isn't always obvious. It can start with uncomfortable comments and escalate to threats. It might be someone constantly messaging you after you've asked them to stop, or spreading false information about you online.",
                    "Cyberstalking is when someone persistently monitors your online activity and contacts you despite your wishes. Doxing is when someone publishes your private information—like your address or phone number—without consent. Both are serious violations of your safety."
                ]
            },
            {
                "title": "Trust Your Instincts",
                "paragraphs": [
                    "If someone's online behavior makes you uncomfortable, that feeling is valid. You don't need to justify why something bothers you. Harassment isn't always threats—it can be persistent unwanted attention that makes you feel unsafe.",
                    "Pay attention to patterns. Does someone show up on multiple platforms? Do they mention things about your life they shouldn't know? These are warning signs that someone is monitoring you more closely than is appropriate."
                ]
            },
            {
                "title": "What to Do Right Now",
                "paragraphs": [
                    "Don't engage with the harasser. Any response, even telling them to stop, can encourage them to continue. Instead, document everything. Take screenshots with dates and times. Save messages and posts. This evidence is crucial if you need to report the harassment.",
                    "Block the person on every platform. Adjust your privacy settings to limit who can contact you and see your content. Make your accounts private if they aren't already."
                ]
            },
            {
                "title": "Getting Help",
                "paragraphs": [
                    "You don't have to handle this alone. Report the harassment to the platform—every social media site has reporting tools. If the harassment involves threats or stalking, contact law enforcement. Bring your documentation with you.",
                    "Talk to someone you trust. Whether it's a friend, family member, or counselor, having support makes a difference. Organizations that specialize in online harassment can provide guidance specific to your situation."
                ]
            },
            {
                "title": "Supporting Someone Else",
                "paragraphs": [
                    "If someone tells you they're being harassed, believe them. Don't ask what they did to cause it—harassment is never the victim's fault. Listen without judgment and offer practical help like assisting with documentation or accompanying them to file a report.",
                    "Don't engage with the harasser yourself. This often makes things worse. The best way to help is to support the person being harassed, not to confront the harasser."
                ]
            },
            {
                "title": "Remember This",
                "paragraphs": [
                    "Online harassment is real, and its effects are serious. You deserve to use the internet without fear. The harassment is not your fault, and you have every right to seek help and protection.",
                    "Recovery takes time. Be patient with yourself. There's no right way to respond to harassment—do what feels safest for you."
                ]
            }
        ]
    }
    lesson2.quiz = [
        {
            "question": "What should you do first if someone is harassing you online?",
            "options": [
                "Respond and tell them to stop",
                "Document everything with screenshots",
                "Delete all your accounts",
                "Ignore it completely"
            ],
            "correct_answer": 1,
            "explanation": "Documentation is crucial. Take screenshots with dates and times before doing anything else. This evidence is essential for reporting and potential legal action."
        },
        {
            "question": "Is online harassment ever the victim's fault?",
            "options": [
                "Yes, if they posted something controversial",
                "Yes, if they didn't use privacy settings",
                "No, it's always the harasser's responsibility",
                "It depends on the situation"
            ],
            "correct_answer": 2,
            "explanation": "Harassment is never the victim's fault, regardless of what they posted or their privacy settings. The responsibility always lies with the person doing the harassing."
        },
        {
            "question": "Why shouldn't you engage with someone harassing you?",
            "options": [
                "Because it's rude",
                "Because any response often encourages them to continue",
                "Because they'll feel bad",
                "Because blocking is easier"
            ],
            "correct_answer": 1,
            "explanation": "Harassers often want any reaction. Responding typically encourages them to continue or escalate. The best approach is to document, block, and report without engaging."
        }
    ]
    lesson2.save()
    print(f"✓ Updated Lesson 2: {lesson2.title}")
    
    # Lesson 3: Securing Your Social Media
    lesson3 = Lesson.objects.get(id=3)
    lesson3.content = {
        "sections": [
            {
                "title": "Why Social Media Security Matters",
                "paragraphs": [
                    "Social media platforms know a lot about you—your relationships, interests, location, and daily patterns. In the wrong hands, this information can be used to track you, manipulate you, or harm you.",
                    "The platforms themselves profit from your data, so their default settings often share more than you'd want. Taking control of your social media security isn't complicated, but it requires some intentional choices."
                ]
            },
            {
                "title": "Password Protection",
                "paragraphs": [
                    "Your password is the lock on your account. Make it strong: at least 12 characters with a mix of letters, numbers, and symbols. Never use the same password on multiple sites—if one gets hacked, all your accounts are at risk.",
                    "A password manager can generate and store complex passwords for you. You only need to remember one master password. This makes it practical to have truly strong, unique passwords everywhere."
                ]
            },
            {
                "title": "Two-Factor Authentication",
                "paragraphs": [
                    "Two-factor authentication (2FA) adds a second security step after your password. Even if someone gets your password, they can't access your account without the code sent to your phone or generated by an authentication app.",
                    "Enable 2FA on every social media account. Yes, it's an extra step when logging in, but it dramatically reduces the risk of unauthorized access. Most platforms remember trusted devices, so you won't need to enter a code every time."
                ]
            },
            {
                "title": "Privacy Settings That Matter",
                "paragraphs": [
                    "Make your accounts private. This means only approved followers can see your posts. Control who can contact you, comment on your posts, and tag you in photos. Hide your email address and phone number from your profile.",
                    "Turn off location tagging. Sharing where you are in real-time tells people your current location and that you're not home. If you want to share where you've been, wait until you've left."
                ]
            },
            {
                "title": "Think Before You Share",
                "paragraphs": [
                    "Once something is online, you can't fully control it. Screenshots exist forever. Before posting, ask yourself: Would I be comfortable with anyone seeing this? Could this reveal information about my location or routine?",
                    "Check photo backgrounds for identifying details like street signs or house numbers. Be especially careful about sharing information about children. What seems harmless now might not be later."
                ]
            },
            {
                "title": "Spotting Scams",
                "paragraphs": [
                    "Be skeptical of messages claiming your account will be deleted unless you verify information. Legitimate platforms don't ask for passwords through direct messages. If something seems urgent or too good to be true, it probably is.",
                    "Fake giveaways, romance scams, and investment schemes are common on social media. Don't click links from people you don't know. Even links from friends should be approached cautiously—their account might be compromised."
                ]
            },
            {
                "title": "Regular Maintenance",
                "paragraphs": [
                    "Review your privacy settings every few months. Platforms change their options, sometimes resetting your preferences. Check which third-party apps have access to your accounts and remove any you don't use or trust.",
                    "Google yourself occasionally to see what information about you is publicly available. Delete old accounts you no longer use. Each small action contributes to your overall security and safety online."
                ]
            }
        ]
    }
    lesson3.quiz = [
        {
            "question": "Why should you use different passwords for each account?",
            "options": [
                "To make them harder to remember",
                "So one security breach doesn't compromise all your accounts",
                "Because websites require it",
                "To confuse hackers"
            ],
            "correct_answer": 1,
            "explanation": "Using unique passwords means that if one service is breached, your other accounts remain secure. This is one of the most effective ways to protect yourself online."
        },
        {
            "question": "What does two-factor authentication do?",
            "options": [
                "Makes logging in faster",
                "Eliminates the need for passwords",
                "Requires a second verification step beyond your password",
                "Automatically backs up your account"
            ],
            "correct_answer": 2,
            "explanation": "Two-factor authentication adds a second layer of security. Even if someone gets your password, they can't access your account without the second factor."
        },
        {
            "question": "When is it safe to share your location on social media?",
            "options": [
                "In real-time so friends know where you are",
                "After you've left the location",
                "Anytime during the day",
                "Location sharing is always safe"
            ],
            "correct_answer": 1,
            "explanation": "Share your location only after you've left. Real-time location sharing tells people where you are right now and that you're not home, which can create safety risks."
        }
    ]
    lesson3.save()
    print(f"✓ Updated Lesson 3: {lesson3.title}")
    
    print("\n✅ All lessons updated with concise, actionable content!")
    print("\nLesson Summary:")
    for lesson in Lesson.objects.all().order_by('id'):
        print(f"\n{lesson.id}. {lesson.title}")
        print(f"   Category: {lesson.category} | Difficulty: {lesson.difficulty}")
        print(f"   Duration: {lesson.duration_minutes} minutes")
        print(f"   Sections: {len(lesson.content.get('sections', []))}")
        print(f"   Quiz questions: {len(lesson.quiz)}")


if __name__ == '__main__':
    update_lessons()
