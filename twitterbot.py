from markov import *


chain_dict = make_chains()
print make_text(chain_dict)


status = api.PostUpdate(make_text(chain_dict))


