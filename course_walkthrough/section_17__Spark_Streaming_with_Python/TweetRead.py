#!/usr/bin/env python
# coding: utf-8

# # Spark Streaming Twitter Project, Part Two
#
# Our next task is to write a script that will connect to Twitter for streaming
#
# This will be a .py file that we will call later on.
#
# Let's get started!

from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
import socket
import json

consumer_key = ""
consumer_secret = ""
access_token = ""
access_secret = ""


# Create a class that will listen to the tweets themselves.
# Create a function that sends the data through a socket.
class TweetListener(StreamListener):
    def __init__(self, csocket):
        self.client_socket = csocket

    def on_data(self, data):
        try:
            msg = json.loads(data)
            print(msg["text"].encode('utf-8'))
            self.client_socket.send(msg['text'].encode('utf-8'))
            # send through socket.
            return True
        except BaseException as e:
            print("ERROR ", e)
        return True

    def on_error(self, status):
        print(status)
        return True


def sendData(c_socket):  # Takes in a client socket.  Connecting everything.
    # Launching a Twitter Stream.  Filter out those tweets for whatever track
    # you have specified.
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    twitter_stream = Stream(auth, TweetListener(csocket=c_socket))
    twitter_stream.filter(track=["piano"])
    # Basically the topic that you can pick


if __name__ == "__main__":  # Essentially a way you can make files run.
    s = socket.socket()  # Setup the socket.
    host = "127.0.0.1"  # localhost, which is your local machine.
    port = 5555  # reserving a port for our connection service.
    s.bind((host, port))

    print("Listening on port 5555")

    s.listen(5)
    c, addr = s.accept()  # That will establish a connection with the client.

    sendData(c)  # Send the data to the client socket.
