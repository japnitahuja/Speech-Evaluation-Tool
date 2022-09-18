from dotenv import load_dotenv
import cohere
import os

def configure():
    load_dotenv()

def main():
    configure()
    co = cohere.Client(os.getenv('api_key'))
    response = co.generate(
        model='xlarge',
        prompt="Hey there. So in my last video, I talked about giving a self introduction presentation and I talked about the importance of relating who you are to your audience to make sure that they will be engaged with what you are talking about and really care about who you are as a person. In this video, I want to talk about what you can say specifically when you are giving your self introduction. This channel here is all about learning presentation skills. I will teach you how tos tips and tricks to give better presentations. You will also see some of my work videos. I own a company called Quan Multimedia, which is a video marketing agency. So you will see some of those videos here too. But for the most part you will get presentations, videos here to help you give better presentations. So make sure you like and subscribe and hit that bell icon as well. Okay? So when you have to give a 62nd selfintroduction, first of all, where would this even take place? Well, a lot of times this takes place in business meetings. It could take place when you are doing an interview. Maybe you are in front of a school group or something like that and you need to just tell people who you are. So what you can say is you can start off with saying your name and saying who you are as far as your job or your title or what you are studying, something like that. So you might say, Hi, my name is Carl, I am an MBA student from the University of California and I am currently studying mechanical engineering, something like that. So that would be a really great start. Now the next part of it is you can talk about something that maybe you specialize in or maybe why you decided to study that just to give people a little bit of background as to who you are as a person. So you could say something like, when I was a child, I really loved putting things together and making things and tinkering with things. And I always just knew how things went together and it was always so boring for me to just sit in the classroom and not be able to make anything. I was most at home when I made something and built things and designed things. And that is what led me to becoming an engineering student. So the next part of it now is to tell people, OK, this is what I am here for, this is why I am here, this is why I am giving the presentation and why I am speaking to you guys today. So one thing you could say if we are talking about this mechanical engineering person is to say today I want to talk about something that is going to be really interesting to give you a better perspective on what we do as mechanical engineers. And it might even spark a little bit of interest and curiosity in becoming an engineer or at least knowing more about engineering yourself. So that's what you have to do to sort of wrap up that 62nd introduction. Just talk about an objective or a goal or maybe something you want the audience to do. It's just a little way of, like, saying, okay, well, here's where I am, here's where I came from, and now here's where we're going with this. So it's just a neat little tidy way to have three sections of the presentation to give that 62nd introduction. Now, just as a final tip here, a 62nd introduction is approximately 150 words. So if you write it out exactly what we want to say word for word, and you're hitting about 150 words, that is perfect. Anything above that, you're going to start speaking a little bit too fast, and it might be hard for people to understand you a little bit slower than that. Then you won't come up to 60 seconds, which is also really good because nobody will complain if your presentation is less than 60 seconds. All right. Anyway anyway, hopefully that is helpful for you. Please let me know if you have any questions or comments about that, and go ahead and try it and let me know how it works for you as well. All right, thanks, and we'll see you in the next video. Bye.", 
        max_tokens=50,
        temperature=0.8,
        k=0,
        p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=["--"],
        return_likelihoods='NONE')
    print('Prediction: {}'.format(response.generations[0].text))

main()