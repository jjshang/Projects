import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

play = pd.read_csv("/Users/jennyshang/Documents/Masters/Masters/Fall 2019/DSO599/Data Project 2/anonymized_activity_play_data_2017_10_01.csv")
member = pd.read_csv("/Users/jennyshang/Documents/Masters/Masters/Fall 2019/DSO599/Data Project 2/anonymized_member_data.csv")

play.head(2)
member.head(2)
play.shape
member.shape

play = play.merge(member, left_on = play.MEMBER_ID, right_on = member.MEMBER_ID)
play["Completion_rate"] = play.NUMBER_OF_ROUNDS_COMPLETED/play.NUMBER_OF_ROUNDS_STARTED
play["Success_rate"] = play.NUMBER_OF_PASSED_ROUNDS/play.NUMBER_OF_ROUNDS_COMPLETED
play.to_csv("Combined_data.csv")
play.head()

play.describe()

play.columns.unique()

plt.figure()
plt.scatter("ADAPTIVE_SCORE", "ACTIVITY_DURATION", data = play)
plt.show()

play1 = play.groupby("ADAPTIVE_SCORE")["ACTIVITY_DURATION"].mean().reset_index()


plt.figure()
plt.scatter(play1.ADAPTIVE_SCORE, play1.ACTIVITY_DURATION)
plt.show()


plt.figure()
plt.hist("ADAPTIVE_SCORE", data = play)
plt.show()

plt.figure()
plt.hist("ACTIVITY_DURATION", data = play)
plt.show()

plt.figure()
plt.scatter("ADAPTIVE_SCORE", "NUMBER_OF_PASSED_ROUNDS", data = play)
plt.show()


play2 = play.groupby("NUMBER_OF_PASSED_ROUNDS")["ADAPTIVE_SCORE"].mean().reset_index()
play2

plt.figure()
plt.scatter(play2.NUMBER_OF_PASSED_ROUNDS,play2.ADAPTIVE_SCORE)
plt.show()

play3 = play.groupby("NUMBER_OF_PASSED_ROUNDS")["ACTIVITY_DURATION"].mean().reset_index()

plt.figure()
plt.scatter(play3.NUMBER_OF_PASSED_ROUNDS,play3.ACTIVITY_DURATION)
plt.show()
## Average activity duration peaks as people pass 4 rounds --> learning curve

play4 = play.groupby("NUMBER_OF_ROUNDS_COMPLETED")["ACTIVITY_DURATION"].mean().reset_index()

plt.figure()
plt.scatter(play4.NUMBER_OF_ROUNDS_COMPLETED,play4.ACTIVITY_DURATION)
plt.show()


play4 = play.groupby("NUMBER_OF_FAILED_ROUNDS")["ACTIVITY_DURATION"].mean().reset_index()

plt.figure()
plt.scatter(play4.NUMBER_OF_FAILED_ROUNDS,play4.ACTIVITY_DURATION)
plt.show()

play.groupby("ACTIVITYPLAY_OUTCOME")["NUMBER_OF_SUBMITS"].sum()
play.groupby("ACTIVITYPLAY_OUTCOME").count()
## People who cancel submit on average 2.306 times. People who succeed submit on average 8.62 times

plt.figure()
plt.scatter("NUMBER_OF_SUBMITS", "POINTS_EARNED", data = play)
plt.show()

play.groupby("STARS_EARNED")["ACTIVITY_DURATION"].mean()

play.groupby("POINTS_EARNED")["ACTIVITY_DURATION"].mean()

play.groupby("ACTIVITY_DIFFICULTY_ID")["ACTIVITY_DURATION"].mean()

play["ACTIVITYPLAY_OUTCOME_NUM"] = play["ACTIVITYPLAY_OUTCOME"].map({"succeed":1, "cancel":0})

play.groupby("ACTIVITY_ID").mean()
play.groupby("ACTIVITY_ID")["ACTIVITYPLAY_OUTCOME_NUM"].mean().max()
play.groupby("ACTIVITY_ID")["ACTIVITYPLAY_OUTCOME_NUM"].mean().min()

play[play.ACTIVITY_DURATION<60].ACTIVITYPLAY_OUTCOME_NUM.sum()/play.ACTIVITY_DURATION.count()
## 19% have successful play within 1 min
play[play.ACTIVITY_DURATION<60].ACTIVITYPLAY_OUTCOME_NUM.count()/play.ACTIVITY_DURATION.count()
## 36% play for less than 1 min
play[play.ACTIVITY_DURATION<60].ADAPTIVE_SCORE.mean()
play[play.ACTIVITY_DURATION<60].NUMBER_OF_ROUNDS_STARTED.mean()
play[play.ACTIVITY_DURATION<60].NUMBER_OF_SUBMITS.mean()
play[play.ACTIVITY_DURATION<60].POINTS_EARNED.mean()

play[play.ACTIVITY_DURATION>=60].ACTIVITYPLAY_OUTCOME_NUM.sum()/play.ACTIVITY_DURATION.count()
## 52% have successful play over 1 min
play[play.ACTIVITY_DURATION>=60].ACTIVITYPLAY_OUTCOME_NUM.count()/play.ACTIVITY_DURATION.count()
play[play.ACTIVITY_DURATION>60].ADAPTIVE_SCORE.mean()
play[play.ACTIVITY_DURATION>60].NUMBER_OF_ROUNDS_STARTED.mean()
play[play.ACTIVITY_DURATION>60].NUMBER_OF_SUBMITS.mean()
play[play.ACTIVITY_DURATION>60].POINTS_EARNED.mean()

play.groupby("VERSION")["MEMBER_ID_x"].count()

cancel = play[play.ACTIVITYPLAY_OUTCOME == "cancel"]
cancel.groupby("ACTIVITY_DIFFICULTY_ID")["NUMBER_OF_ROUNDS_STARTED"].count()

play.groupby("NUMBER_OF_PASSED_ROUNDS")["MEMBER_ID_x"].count()
play.MEMBER_ID_x.count()
(84283+58716+29606)/269560

play6 = play.groupby("MEMBER_ID_x")[["ACTIVITY_DURATION","NUMBER_OF_SUBMITS","NUMBER_OF_FAILED_ROUNDS","NUMBER_OF_PASSED_ROUNDS","NUMBER_OF_ROUNDS_COMPLETED","NUMBER_OF_ROUNDS_STARTED"]].sum().reset_index()

plt.figure()
plt.scatter("NUMBER_OF_PASSED_ROUNDS","ACTIVITY_DURATION", data = play6)
plt.show()
plt.figure()
plt.scatter("NUMBER_OF_ROUNDS_COMPLETED","ACTIVITY_DURATION", data = play6)
plt.show()
plt.figure()
plt.scatter("NUMBER_OF_FAILED_ROUNDS","ACTIVITY_DURATION", data = play6)
plt.show()
plt.figure()
plt.scatter("NUMBER_OF_FAILED_ROUNDS","NUMBER_OF_SUBMITS", data = play6)
plt.show()

plt.figure()
plt.scatter("NUMBER_OF_PASSED_ROUNDS","NUMBER_OF_SUBMITS", data = play6)
plt.show()

play.groupby("ACTIVITY_RANGE")["MEMBER_ID_x"].count()
