import requests
import smtplib
from post import Post
from flask import Flask, render_template, request


app = Flask(__name__)
all_posts = requests.get('https://api.npoint.io/a8139e465070da1aa2a3').json()
posts = []
for post in all_posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"], post["author"], post["date"], post["image"])
    posts.append(post_obj)


@app.route("/")
def index():
    return render_template("index.html", all_posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        # send an email
        my_mail = "cedricbenonga13@gmail.com"
        my_password = "hnburjdualyyopbm"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_mail, password=my_password)
            connection.sendmail(
                from_addr=my_mail,
                to_addrs=my_mail,
                msg=f"subject:From Blog Website\n\n{name}\n{email}\n{phone}\n{message}"
            )

        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route("/post")
def post():
    return render_template("post.html")


@app.route("/poster/<int:index>")
def posters(index):

    poster = None
    for blog_post in posts:
        if blog_post.id == index:
            poster = blog_post

    return render_template("posters.html", poster=poster)


if __name__ == "__main__":
    app.run(debug=True)


# https://www.npoint.io/docs/a8139e465070da1aa2a3 --> personal API
# https://bootstrapmade.com/ --> bootstrap templates (best)
# https://getbootstrap.com/docs/5.3/examples/ --> bootstrap templates
# https://bootsnipp.com/search?q=login+sample&page=2 --> bootstrap parts templates
# https://fontawesome.com/icons/envelope?s=solid&f=classic --> icons
# https://unsplash.com/ --> Nice photos
# https://www.creative-tim.com/bootstrap-themes/free --> Free Bootstrap templates
