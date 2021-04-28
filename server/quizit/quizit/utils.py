from .db import Cursor
import json 

# USERS

class CheckAuthentication:
    def checkIfPassowordAndHashedMatches(self, password,hashed):
        pass

    def checkIfPasswordAndUsernameMatches(self, username, password):
        print(username, password)
    
    def chechIfPasswordAndEmailMatches(self, email, password):
        pass

class RegisterUser(CheckAuthentication):
    def post(self, **kwargs):
        pass

    def hashPassword(self, password):
        pass

class LoginUser(CheckAuthentication):
    def put(self, token, id):
        pass

class LogoutUser(CheckAuthentication):
    def get(self, id, password):
        pass

    def put(self, id):
        pass

class EditUser(CheckAuthentication):
    def get(self, id,password):
        pass

    def put(self, **kwargs):
        pass

class DeleteUser(CheckAuthentication):
    def get(self, id,password):
        pass

    def delete(self, id):
        pass

# QUIZES

class CheckQuizes:
    def getQuestions(self, id):
        pass

    def getAnswers(self,id):
        pass

class CreateQuiz(CheckQuizes):
    def post(self,**kwargs):
        pass

    def createAnswers(self, **kwargs):
        pass

    def createQuestions(self, **kwargs):
        pass

class EditQuiz(CheckQuizes):
    def put(self,**kwargs):
        pass

    def editQuestions(self, **kwargs):
        pass

    def editAnswers(self, **kwargs):
        pass

class DeleteQuiz(CheckQuizes):
    def delete(self, id):
        pass

    def deleteQuestions(self, id):
        pass

    def deleteAnswers(self, id):
        pass

class GetAllQuizes:
    def get(self):
        pass

class GetOneQuiz:
    def get(self,id):
        pass

class GetBySearch:
    def get(self, query):
        pass

class GetByRating:
    def get(self):
        pass

class GetByCategory:
    def get(self,category):
        pass

class GetByDifficulty:
    def get(self, difficulty=None):
        pass

class GetBySubscribers:
    def get(self, id):
        pass

# STATS 

class AddStats:
    def post(self, **kwargs):
        pass

class DeleteStats:
    def delete(self, id):
        pass

class EditStats:
    def put(self, **kwargs):
        pass

class GetStats:
    def get(self,id):
        pass
# LEADERBOARD 

class CreateLeaderBoard:
    def post(self, **kwargs):
        pass

class DeleteLeaderBoard:
    def delete(self, id):
        pass

class EditLeaderBoard:
    def put(self,**kwargs):
        pass

class GetLeaderBoard:
    def get(self, id):
        pass

# COMMENTS 

class AddComment:
    def post(self, **kwargs):
        pass

class EditComment:
    def put(self, **kwargs):
        pass

class DeleteComment:
    def delete(self, id):
        pass

class GetCommentsForQuiz:
    def get(self, id):
        pass

class GetCommentsForUser:
    def get(self, id):
        pass

class GetOneComment:
    def get(self, id):
        pass

# RATINGS 

class AddRating:
    def post(self, **kwargs):
        pass

class EditRating:
    def put(self, **kwargs):
        pass

class DeleteRating:
    def delete(self, id):
        pass

class GetRatingForQuiz:
    def get(self, id):
        pass

class GetRatingForUser:
    def get(self, id):
        pass

class GetOneRating:
    def get(self, id):
        pass

# SUBSCRIBERS 

class Subscribe:
    def post(self, **kwargs):
        pass

class Unsubscribe:
    def delete(self, user_1,user_2):
        pass

class GetSubscribersForUser:
    def get(self, id):
        pass