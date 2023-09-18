css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://imgs.search.brave.com/aU7SbN6RMMtMuWLiYQ_p5qokNtxptjCvbDc8bXqry4Y/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvOTc3/Mjk2NDQvcGhvdG8v/YmFiYS1yYW1kZXYt/YXQtdGhlLXNlY29u/ZC1kYXktb2YtdGhl/LWluZGlhLXRvZGF5/LWNvbmNsYXZlLWlu/LW5ldy1kZWxoaS1v/bi1tYXJjaC0xMy0y/MDEwLmpwZz9zPTYx/Mng2MTImdz0wJms9/MjAmYz1aMXZZTlA3/SzFTeGhDWU9rd1pr/Y0IwTDd1VkVkMjdv/LUkzQmtnQWxGU3Vj/PQ" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://imgs.search.brave.com/QoTS4n1qAdzE0QGaaUHXpuyjwUy4cOXGqsOj_6XKR8g/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9tLm1l/ZGlhLWFtYXpvbi5j/b20vaW1hZ2VzL0kv/NTFkMDZ4bDlBekwu/anBn">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''