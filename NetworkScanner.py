#Allows us to connect to different servers on a certain socket on a certain port.
import socket
#Allows us to wrap our socket connection in SSL
import ssl
#Keep track of server uptime
from datetime import datetime
#Allows us to ping computers
import subprocess
import platform

#Class name
class Server():
    #Instance variables required for port scanning
    def __init__(self, name, port, connection, priority):
        self.name = name
        self.port = port
        self.connection = connection.lower()
        self.priority = priority.lower()

        self.history = []
        self.alert = False
    #Tests connection
    def check_connection(self):
        #Used to print out connection attempt results
        msg = ""
        #We will be assuming all the connections are false initally until tested
        success = False
        #Current time
        now = datetime.now()

        #Using a try except block to attempt connecting to unqiue ports and print out results
        try:
            if self.connection == "plain":
                #Connects to socket bu passing in desination address+port and timeout value in seconds
                socket.create_connection((self.name, self.port), timeout=10)
                msg = f"{self.name} is up. On port {self.port} with {self.connection}"
                success = True
                self.alert = False
            elif self.connection == "ssl":
                #Given a connection oriented socket this returns a SSLSocket after it copies the attributes/options of the socket instance its wrapped around
                ssl.wrap_socket(socket.create_connection((self.name, self.port), timeout=10))
                msg = f"{self.name} is up. On port {self.port} with {self.connection}"
                success = True
                self.alert = False
            else:
                #Ping function defined below, so this else statement will only run if we successfully ping the server printing out our success
                if self.ping():
                    msg = f"{self.name} is up. On port {self.port} with {self.connection}"
                    success = True
                    self.alert = False
        #Prints out server timeout information if the request isnt refused but also not successful {e} - is the error message we would recieve
        except socket.timeout:
            msg = f"server: {self.name} timeout. On port {self.port}"
        #Prints out server error information if connection is refused {e} - is the error message we would recieve
        except (ConnectionRefusedError, ConnectionResetError) as e:
            msg = f"server: {self.name} {e}"
        #Worst case scenario unknown error message {e} - is the error message we would recieve
        except Exception as e:
            msg = f"No Clue??: {e}"


        self.create_history(msg,success,now)
    #Used to initialize maximum number of history saved
    def create_history(self, msg, success, now):
        history_max = 100
        self.history.append((msg,success,now))
        #Will continute to fill out list until it reaches history_max
        while len(self.history) > history_max:
            self.history.pop(0)

             

    def ping(self):
        try:
            output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower(
            ) == "windows" else 'c', self.name ), shell=True, universal_newlines=True)
            if 'unreachable' in output:
                return False
            else:
                return True
        except Exception:
                return False

#Makes sure CheckServer is the main program being run
if __name__ == "__main__":

    
        #List of servers we will be scanning
    servers = [

        Server("reddit.com", 80, "plain", "high"),
        Server("msn.com", 80, "plain", "high"),
        Server("bing.com", 80, "plain", "high"),
        Server("outlook.com", 80, "plain", "high"),
        Server("Amazon.com", 80, "plain", "high"),
        Server("Instagram.com", 80, "plain", "high"),
        Server("youtube.com", 80, "plain", "high"),
        Server("Facebook.com", 80, "plain", "high"),
        Server("Wikipedia.org", 80, "plain", "high"),
        Server("yahoo.com", 80, "plain", "high"),    
        Server("ebay.com", 80, "plain", "high"),
        Server("walmart.com", 80, "plain", "high"),
        Server("twitter.com", 80, "plain", "high"),
        Server("cnn.com", 80, "plain", "high"),
        Server("twitch.com", 80, "plain", "high"),
        Server("espn.com", 80, "plain", "high"),
        Server("netflix.com", 80, "plain", "high"),
        Server("zillow.com", 80, "plain", "high"),
        Server("office.com", 80, "plain", "high"),
        Server("usps.com", 80, "plain", "high"),
        Server("paypal.com", 80, "plain", "high"),
        Server("google.com", 80, "plain", "high"),
        Server("wit.edu", 80, "plain", "high")
    ]
    #Runs the program for each server in the server list
    for server in servers:
        server.check_connection()
        #Prints out history 

        print(server.history[-1])
#datetime(year, month, day, hour, minute, second, microsecond)
