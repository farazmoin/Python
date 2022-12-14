import praw
import config
from textblob import TextBlob
from bitfinex import WssClient, ClientV2, ClientV1

# bfx_client = ClientV2(config.bitfinex_key, config.bitfinex_secret)
#
# wallet_balance = bfx_client.wallets_balance()
# print('Current Balance: ')
# xrp_price = bfx_client.tickers(['tXRPUSD'])
# for i in wallet_balance:
#     if round(i[2]) == 0.00:
#         continue
#     else:
#         if i[1] == 'XRP':
#             print(i[1], round(i[2]), '|', 'Low: ', xrp_price[0][-1], '|', 'High', xrp_price[0][-2], '|', 'Last price: ', xrp_price[0][-4], '\n')
#
# active_orders = bfx_client.active_orders()
# print('Active Orders : ')
# for i in active_orders:
#     print('Order Id: ', i[0], 'Symbol: ', i[3], 'Amount: ', i[6], 'Price: ', i[16])
#
# # bfx_client.submit_order("LIMIT", "tXRPUSD", "0.3500", "10");
#
# # bfx_client.cancel_order(id=105197668321)
#
# pos_info = bfx_client.active_positions()
# print('\n')
# print('Open Positions: ')
# print('Symbol : ', pos_info[0][0], 'Units : ', pos_info[0][2], 'Price : ', pos_info[0][3], 'PNL : ', round(pos_info[0][6]))


reddit = praw.Reddit(
    client_id=config.reddit_id,
    client_secret=config.reddit_secret,
    password=config.reddit_password,
    user_agent="USERAGENT",
    username=config.reddit_username,
)

sentimentLst = list()
neededSentiment = 100


def average(lst):
    if len(lst) == 0:
        return len(lst)
    else:
        return sum(lst[-neededSentiment:]) / neededSentiment


for comment in reddit.subreddit("cryptocurrency+xrp+bitcoin").stream.comments():
    redditComments = comment.body
    blob = TextBlob(redditComments)
    sentiment = blob.sentiment

    if sentiment.polarity != 0.0:
        sentimentLst.append(sentiment.polarity)

        print('Total Sentiment is: |||||| ', average(sentimentLst))

        if len(sentimentLst) > neededSentiment and average(sentimentLst) > 0.50:
            print('Buy Detected based on sentiment analysis')

