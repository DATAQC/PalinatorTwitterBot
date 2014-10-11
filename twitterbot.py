from markov import *
import twitter
from secrets import *

api = twitter.Api()

api = twitter.Api(consumerkey,
consumersecret, accesstoken, accesstokensecret)

print api.VerifyCredentials()

chain_dict = make_chains()
print make_text(chain_dict)


status = api.PostUpdate(make_text(chain_dict))


