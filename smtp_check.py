import smtplib
import ssl

def check_smtp_connection(
    host,
    port,
    username=None,
    password=None,
    encryption="none",  # "none", "ssl", or "tls"
    timeout=10
):
    try:
        if encryption.lower() == "ssl":
            context = ssl.create_default_context()
            server = smtplib.SMTP_SSL(host, port, timeout=timeout, context=context)
        else:
            server = smtplib.SMTP(host, port, timeout=timeout)

        server.set_debuglevel(0)  # set to 1 to see SMTP conversation

        if encryption.lower() == "tls":
            #context = ssl.create_default_context() 
            context = ssl._create_unverified_context() # Do not do in production !
            server.starttls(context=context)

        if username and password:
            server.login(username, password)

        server.noop()  # simple command to verify connection
        server.quit()

        print(f"✅ SMTP connection successful ({encryption.upper()})")
        return True

    except Exception as e:
        print(f"❌ SMTP connection failed ({encryption.upper()}): {e}")
        return False


if __name__ == "__main__":
    HOST = ""
    PORT = 25  # 25 (none), 465 (ssl), 587 (tls)
    USERNAME = ""
    PASSWORD = ""

    # Test different connection types
    #check_smtp_connection(HOST, 25, USERNAME, PASSWORD, "none")
    #check_smtp_connection(HOST, 465, USERNAME, PASSWORD, "ssl")
    check_smtp_connection(HOST, PORT, USERNAME, PASSWORD, "tls")