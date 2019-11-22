import discord, os

TOKEN = os.getenv("BRAIN_TOKEN")

BRAIN = discord.Client()

PREFIX = "tc/"

STAFF_ID = 481991172106092554
TWOW_CENTRAL_ID = 481509601590771724
MEMBER_ID = 481950361783894017

PUBLIC_CHANNELS = (
	481509602035236865, #general
	481534463608619038, #rec-room
	598616636823437352, #game-room
	481535292541501452, #twow-discussion
	481534865045717013, #art-studio
	481534925997211658, #server-discussion
	481534942279630856, #bots-memes
	534909693580017685, #voting
	481535329199980564, #general-hosting
	481549073401511952, #aesthetics
	481549091298344961, #technologies
	481549106662211588, #presentation
	481549059656777739, #innovations
	614117909693857819  #vc-general
)

BOT_CHANNELS = (
	481534942279630856
)

LOG_CHANNEL = 587038853315952666