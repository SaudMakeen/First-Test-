from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Saud Portal</title>

        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                font-family: Arial, sans-serif;
                background: linear-gradient(1000deg, #38bdf8, #ec4899);
            }
            @keyframes fadeInUp {
            
                from {
                    opacity: 0;
                    transform: translateY(60px);
                }
            
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            
            }
            .login-box {
                width: 350px;
                background: linear-gradient(1000deg, #ec4899, #38bdf8);
                border-radius: 12px;
                padding: 40px;
                text-align: center;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
                animation: fadeInUp 1s ease-out;
                transition: all 0.3s ease;
            }
            
            .login-box:hover {
                background: White;
                transform: scale(1.02);
            }
    
            .login-box:hover .logo {
                
                    background: linear-gradient(1000deg, #38bdf8, #ec4899);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
            }
            
            .logo {
                font-size: 50px;
                font-weight: bold;
                font-family: 'Nunito', sans-serif;
                background: White;
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            
                transition: all 0.3s ease;
            }

            h2 {
                color: #444;
                margin-bottom: 25px;
            }

            input {
                width: 100%;
                padding: 12px;
                margin-bottom: 15px;
                border: 1px solid #ccc;
                border-radius: 5px;
                box-sizing: border-box;
            }

            button {
                width: 100%;
                padding: 12px;
                border: none;
                border-radius: 5px;
                background: #ffffff;
                color:#38bdf8 ;
                font-weight: bold;
                font-size: 16px;
                cursor: pointer;
                
            }

            button:hover {
                background: linear-gradient(90deg, #ec4899, #38bdf8);
                color:white;
            }

            .footer {
                margin-top: 20px;
                font-size: 12px;
                color: gray;
            }
        </style>

    </head>

    <body>

        <div class="login-box">

            <div class="logo">
                Zain Saud
            </div>

            <h2> Discover More </h2>

            <input type="text" placeholder="Username">

            <input type="password" placeholder="Password">

            <button class="button">Login</button>

            <div class="footer">
                © 2026 Zain Saud Portal
            </div>

        </div>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run()