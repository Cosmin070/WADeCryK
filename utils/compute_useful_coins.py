from images import image_dict

coins = [
    {
        'id': 'acoin',
        'symbol': 'acoin',
        'name': 'Acoin'
    },
    {
        'id': 'alphacoin',
        'symbol': 'alpha',
        'name': 'AlphaCoin'
    },
    {
        'id': 'animecoin',
        'symbol': 'ani',
        'name': 'Animecoin'
    },
    {
        'id': 'antimatter',
        'symbol': 'matter',
        'name': 'AntiMatter'
    },
    {
        'id': 'apecoin',
        'symbol': 'ape',
        'name': 'ApeCoin'
    },
    {
        'id': 'aquariuscoin',
        'symbol': 'arco',
        'name': 'AquariusCoin'
    },
    {
        'id': 'arcticcoin',
        'symbol': 'arc',
        'name': 'Advanced Technology Coin'
    },
    {
        'id': 'aryacoin',
        'symbol': 'aya',
        'name': 'Aryacoin'
    },
    {
        'id': 'audiocoin',
        'symbol': 'adc',
        'name': 'AudioCoin'
    },
    {
        'id': 'auroracoin',
        'symbol': 'aur',
        'name': 'Auroracoin'
    },
    {
        'id': 'bitbar',
        'symbol': 'btb',
        'name': 'Bitbar'
    },
    {
        'id': 'bitcoin',
        'symbol': 'btc',
        'name': 'Bitcoin'
    },
    {
        'id': 'bitgem',
        'symbol': 'xbtg',
        'name': 'Bitgem'
    },
    {
        'id': 'blackcoin',
        'symbol': 'blk',
        'name': 'BlackCoin'
    },
    {
        'id': 'bluecoin',
        'symbol': 'blu',
        'name': 'Bluecoin'
    },
    {
        'id': 'bolivarcoin',
        'symbol': 'boli',
        'name': 'Bolivarcoin'
    },
    {
        'id': 'boost',
        'symbol': 'boost',
        'name': 'Boost'
    },
    {
        'id': 'bunnycoin',
        'symbol': 'bun',
        'name': 'Bunnycoin'
    },
    {
        'id': 'byteball',
        'symbol': 'gbyte',
        'name': 'Obyte'
    },
    {
        'id': 'bytecoin',
        'symbol': 'bcn',
        'name': 'Bytecoin'
    },
    {
        'id': 'cannabiscoin',
        'symbol': 'cann',
        'name': 'CannabisCoin'
    },
    {
        'id': 'carboncoin',
        'symbol': 'carbon',
        'name': 'Carboncoin'
    },
    {
        'id': 'casinocoin',
        'symbol': 'csc',
        'name': 'Casinocoin'
    },
    {
        'id': 'cloudcoin',
        'symbol': 'cc',
        'name': 'CloudCoin'
    },
    {
        'id': 'corgicoin',
        'symbol': 'corgi',
        'name': 'CorgiCoin'
    },
    {
        'id': 'counterparty',
        'symbol': 'xcp',
        'name': 'Counterparty'
    },
    {
        'id': 'cowcoin',
        'symbol': 'cc',
        'name': 'CowCoin'
    },
    {
        'id': 'cpucoin',
        'symbol': 'cpu',
        'name': 'CPUcoin'
    },
    {
        'id': 'credit',
        'symbol': 'credit',
        'name': 'Credit'
    },
    {
        'id': 'credits',
        'symbol': 'cs',
        'name': 'CREDITS'
    },
    {
        'id': 'creds',
        'symbol': 'creds',
        'name': 'Creds'
    },
    {
        'id': 'crevacoin',
        'symbol': 'creva',
        'name': 'Crevacoin'
    },
    {
        'id': 'curecoin',
        'symbol': 'cure',
        'name': 'Curecoin'
    },
    {
        'id': 'denarius',
        'symbol': 'd',
        'name': 'Denarius'
    },
    {
        'id': 'digibyte',
        'symbol': 'dgb',
        'name': 'DigiByte'
    },
    {
        'id': 'digitalcoin',
        'symbol': 'dgc',
        'name': 'Digitalcoin'
    },
    {
        'id': 'dimecoin',
        'symbol': 'dime',
        'name': 'Dimecoin'
    },
    {
        'id': 'dogecoin',
        'symbol': 'doge',
        'name': 'Dogecoin'
    },
    {
        'id': 'doubloon',
        'symbol': 'dbl',
        'name': 'Doubloon'
    },
    {
        'id': 'earthcoin',
        'symbol': 'eac',
        'name': 'Earthcoin'
    },
    {
        'id': 'einsteinium',
        'symbol': 'emc2',
        'name': 'Einsteinium'
    },
    {
        'id': 'electronicgulden',
        'symbol': 'efl',
        'name': 'Electronic Gulden'
    },
    {
        'id': 'emercoin',
        'symbol': 'emc',
        'name': 'EmerCoin'
    },
    {
        'id': 'ethereum',
        'symbol': 'eth',
        'name': 'Ethereum'
    },
    {
        'id': 'exchangecoin',
        'symbol': 'excc',
        'name': 'ExchangeCoin'
    },
    {
        'id': 'exclusivecoin',
        'symbol': 'excl',
        'name': 'ExclusiveCoin'
    },
    {
        'id': 'experiencecoin',
        'symbol': 'epc',
        'name': 'ExperienceCoin'
    },
    {
        'id': 'feathercoin',
        'symbol': 'ftc',
        'name': 'Feathercoin'
    },
    {
        'id': 'fedoracoin',
        'symbol': 'tips',
        'name': 'Fedoracoin'
    },
    {
        'id': 'filecoin',
        'symbol': 'fil',
        'name': 'Filecoin'
    },
    {
        'id': 'flux',
        'symbol': 'flux',
        'name': 'Datamine FLUX'
    },
    {
        'id': 'forexcoin',
        'symbol': 'forex',
        'name': 'FOREXCOIN'
    },
    {
        'id': 'freedomcoin',
        'symbol': 'freed',
        'name': 'Freedomcoin'
    },
    {
        'id': 'freicoin',
        'symbol': 'frc',
        'name': 'Freicoin'
    },
    {
        'id': 'futurecoin',
        'symbol': 'future',
        'name': 'FutureCoin'
    },
    {
        'id': 'gabecoin',
        'symbol': 'gabecoin',
        'name': 'Gabecoin'
    },
    {
        'id': 'galaxycoin',
        'symbol': 'galaxy',
        'name': 'GalaxyCoin'
    },
    {
        'id': 'gamecredits',
        'symbol': 'game',
        'name': 'GameCredits'
    },
    {
        'id': 'gapcoin',
        'symbol': 'gap',
        'name': 'Gapcoin'
    },
    {
        'id': 'geocoin',
        'symbol': 'geo',
        'name': 'Geocoin'
    },
    {
        'id': 'globalboost',
        'symbol': 'bsty',
        'name': 'GlobalBoost-Y'
    },
    {
        'id': 'globalcoin',
        'symbol': 'glc',
        'name': 'GlobalCoin'
    },
    {
        'id': 'goldcoin',
        'symbol': 'glc',
        'name': 'Goldcoin'
    },
    {
        'id': 'graphene',
        'symbol': 'gfn',
        'name': 'Graphene'
    },
    {
        'id': 'greencoin',
        'symbol': 'gre',
        'name': 'Greencoin'
    },
    {
        'id': 'groestlcoin',
        'symbol': 'grs',
        'name': 'Groestlcoin'
    },
    {
        'id': 'gsmcoin',
        'symbol': 'gsm',
        'name': 'GSMcoin'
    },
    {
        'id': 'guncoin',
        'symbol': 'gun',
        'name': 'Guncoin'
    },
    {
        'id': 'harmonycoin',
        'symbol': 'hmc',
        'name': 'HarmonyCoin'
    },
    {
        'id': 'hashcoin',
        'symbol': 'hsc',
        'name': 'HashCoin'
    },
    {
        'id': 'helleniccoin',
        'symbol': 'hnc',
        'name': 'HNC Coin'
    },
    {
        'id': 'herocoin',
        'symbol': 'play',
        'name': 'HEROcoin'
    },
    {
        'id': 'hicoin',
        'symbol': 'xhi',
        'name': 'HiCoin'
    },
    {
        'id': 'hobonickels',
        'symbol': 'hbn',
        'name': 'Hobonickels'
    },
    {
        'id': 'hodlcoin',
        'symbol': 'hodl',
        'name': 'HOdlcoin'
    },
    {
        'id': 'htmlcoin',
        'symbol': 'html',
        'name': 'HTMLCOIN'
    },
    {
        'id': 'i0coin',
        'symbol': 'i0c',
        'name': 'I0Coin'
    },
    {
        'id': 'incakoin',
        'symbol': 'nka',
        'name': 'IncaKoin'
    },
    {
        'id': 'influxcoin',
        'symbol': 'infx',
        'name': 'Influxcoin'
    },
    {
        'id': 'intercoin',
        'symbol': 'itr',
        'name': 'Intercoin'
    },
    {
        'id': 'iocoin',
        'symbol': 'ioc',
        'name': 'I/O Coin'
    },
    {
        'id': 'ion',
        'symbol': 'ion',
        'name': 'Ion'
    },
    {
        'id': 'ixcoin',
        'symbol': 'ixc',
        'name': 'Ixcoin'
    },
    {
        'id': 'jetcoin',
        'symbol': 'jet',
        'name': 'Jetcoin'
    },
    {
        'id': 'joulecoin',
        'symbol': 'xjo',
        'name': 'Joulecoin'
    },
    {
        'id': 'kobocoin',
        'symbol': 'kobo',
        'name': 'Kobocoin'
    },
    {
        'id': 'leafcoin',
        'symbol': 'leaf',
        'name': 'Leafcoin'
    },
    {
        'id': 'lightcoin',
        'symbol': 'lhc',
        'name': 'Lightcoin'
    },
    {
        'id': 'likecoin',
        'symbol': 'like',
        'name': 'LikeCoin'
    },
    {
        'id': 'lisk',
        'symbol': 'lsk',
        'name': 'Lisk'
    },
    {
        'id': 'litebar',
        'symbol': 'ltb',
        'name': 'LiteBar'
    },
    {
        'id': 'litecoin',
        'symbol': 'ltc',
        'name': 'Litecoin'
    },
    {
        'id': 'machinecoin',
        'symbol': 'mac',
        'name': 'Machinecoin'
    },
    {
        'id': 'maidsafecoin',
        'symbol': 'emaid',
        'name': 'MaidSafeCoin'
    },
    {
        'id': 'mapcoin',
        'symbol': 'mapc',
        'name': 'MapCoin'
    },
    {
        'id': 'marscoin',
        'symbol': 'mars',
        'name': 'Marscoin'
    },
    {
        'id': 'martexcoin',
        'symbol': 'mxt',
        'name': 'MarteXcoin'
    },
    {
        'id': 'marxcoin',
        'symbol': 'marx',
        'name': 'MarxCoin'
    },
    {
        'id': 'maxcoin',
        'symbol': 'max',
        'name': 'Maxcoin'
    },
    {
        'id': 'memecoin',
        'symbol': 'mem',
        'name': 'Memecoin'
    },
    {
        'id': 'metacoin',
        'symbol': 'mtc',
        'name': 'Metacoin'
    },
    {
        'id': 'microcoin',
        'symbol': 'mcc',
        'name': 'MicroCoin'
    },
    {
        'id': 'mincoin',
        'symbol': 'mnc',
        'name': 'Mincoin'
    },
    {
        'id': 'mindcoin',
        'symbol': 'mnd',
        'name': 'MindCoin'
    },
    {
        'id': 'mintcoin',
        'symbol': 'mint',
        'name': 'Mintcoin'
    },
    {
        'id': 'monacoin',
        'symbol': 'mona',
        'name': 'MonaCoin'
    },
    {
        'id': 'monero',
        'symbol': 'xmr',
        'name': 'Monero'
    },
    {
        'id': 'mooncoin',
        'symbol': 'moon',
        'name': 'Mooncoin'
    },
    {
        'id': 'motacoin',
        'symbol': 'mota',
        'name': 'MotaCoin'
    },
    {
        'id': 'motocoin',
        'symbol': 'moto',
        'name': 'Motocoin'
    },
    {
        'id': 'myriadcoin',
        'symbol': 'xmy',
        'name': 'Myriad'
    },
    {
        'id': 'namecoin',
        'symbol': 'nmc',
        'name': 'Namecoin'
    },
    {
        'id': 'nest',
        'symbol': 'nest',
        'name': 'Nest Protocol'
    },
    {
        'id': 'netcoin',
        'symbol': 'net',
        'name': 'Netcoin'
    },
    {
        'id': 'nevacoin',
        'symbol': 'neva',
        'name': 'NevaCoin'
    },
    {
        'id': 'newyorkcoin',
        'symbol': 'nyc',
        'name': 'NewYorkCoin'
    },
    {
        'id': 'nexus',
        'symbol': 'nxs',
        'name': 'Nexus'
    },
    {
        'id': 'noblecoin',
        'symbol': 'nobl',
        'name': 'NobleCoin'
    },
    {
        'id': 'novacoin',
        'symbol': 'nvc',
        'name': 'Novacoin'
    },
    {
        'id': 'npccoin',
        'symbol': 'npc',
        'name': 'NPCcoin'
    },
    {
        'id': 'nyancoin',
        'symbol': 'nyan',
        'name': 'Nyancoin'
    },
    {
        'id': 'octocoin',
        'symbol': '888',
        'name': 'Octocoin'
    },
    {
        'id': 'opalcoin',
        'symbol': 'auop',
        'name': 'Opalcoin'
    },
    {
        'id': 'orbitcoin',
        'symbol': 'orb',
        'name': 'Orbitcoin'
    },
    {
        'id': 'orlycoin',
        'symbol': 'orly',
        'name': 'Orlycoin'
    },
    {
        'id': 'osmiumcoin',
        'symbol': 'os76',
        'name': 'OsmiumCoin'
    },
    {
        'id': 'paccoin',
        'symbol': 'pac',
        'name': 'PAC Protocol'
    },
    {
        'id': 'pakcoin',
        'symbol': 'pak',
        'name': 'Pakcoin'
    },
    {
        'id': 'pandacoin',
        'symbol': 'pnd',
        'name': 'Pandacoin'
    },
    {
        'id': 'parallelcoin',
        'symbol': 'duo',
        'name': 'ParallelCoin'
    },
    {
        'id': 'peercoin',
        'symbol': 'ppc',
        'name': 'Peercoin'
    },
    {
        'id': 'petrodollar',
        'symbol': 'xpd',
        'name': 'PetroDollar'
    },
    {
        'id': 'phoenixcoin',
        'symbol': 'pxc',
        'name': 'Phoenixcoin'
    },
    {
        'id': 'pinkcoin',
        'symbol': 'pink',
        'name': 'Pinkcoin'
    },
    {
        'id': 'piratecoin',
        'symbol': 'piratecoin☠',
        'name': 'PirateCoin'
    },
    {
        'id': 'poopcoin',
        'symbol': 'poop',
        'name': 'PoopCoin'
    },
    {
        'id': 'postcoin',
        'symbol': 'post',
        'name': 'PostCoin'
    },
    {
        'id': 'potcoin',
        'symbol': 'pot',
        'name': 'Potcoin'
    },
    {
        'id': 'primecoin',
        'symbol': 'xpm',
        'name': 'Primecoin'
    },
    {
        'id': 'putincoin',
        'symbol': 'put',
        'name': 'PUTinCoin'
    },
    {
        'id': 'quebecoin',
        'symbol': 'qbc',
        'name': 'Quebecoin'
    },
    {
        'id': 'ratecoin',
        'symbol': 'xra',
        'name': 'Ratecoin'
    },
    {
        'id': 'ravencoin',
        'symbol': 'rvn',
        'name': 'Ravencoin'
    },
    {
        'id': 'reddcoin',
        'symbol': 'rdd',
        'name': 'Reddcoin'
    },
    {
        'id': 'riecoin',
        'symbol': 'ric',
        'name': 'Riecoin'
    },
    {
        'id': 'ripple',
        'symbol': 'xrp',
        'name': 'XRP'
    },
    {
        'id': 'ronpaulcoin',
        'symbol': 'rpc',
        'name': 'RonPaulCoin'
    },
    {
        'id': 'sexcoin',
        'symbol': 'sxc',
        'name': 'Sexcoin'
    },
    {
        'id': 'shitcoin',
        'symbol': 'shit',
        'name': 'ShitCoin'
    },
    {
        'id': 'siacoin',
        'symbol': 'sc',
        'name': 'Siacoin'
    },
    {
        'id': 'sibcoin',
        'symbol': 'sib',
        'name': 'SIBCoin'
    },
    {
        'id': 'sjwcoin',
        'symbol': 'sjw',
        'name': 'SJWCoin'
    },
    {
        'id': 'skycoin',
        'symbol': 'sky',
        'name': 'Skycoin'
    },
    {
        'id': 'slimcoin',
        'symbol': 'slm',
        'name': 'Slimcoin'
    },
    {
        'id': 'slothcoin',
        'symbol': 'sloth',
        'name': 'SlothCoin'
    },
    {
        'id': 'smileycoin',
        'symbol': 'smly',
        'name': 'Smileycoin'
    },
    {
        'id': 'songcoin',
        'symbol': 'song',
        'name': 'SongCoin'
    },
    {
        'id': 'spacecoin',
        'symbol': 'space',
        'name': 'Spacecoin'
    },
    {
        'id': 'spartancoin',
        'symbol': 'spn',
        'name': 'SpartanCoin'
    },
    {
        'id': 'sphere',
        'symbol': 'sphr',
        'name': 'Sphere'
    },
    {
        'id': 'spots',
        'symbol': 'spt',
        'name': 'Spots'
    },
    {
        'id': 'starcoin',
        'symbol': 'stc',
        'name': 'Starcoin'
    },
    {
        'id': 'stealthcoin',
        'symbol': 'xst',
        'name': 'Stealth'
    },
    {
        'id': 'steem',
        'symbol': 'steem',
        'name': 'Steem'
    },
    {
        'id': 'stellar',
        'symbol': 'xlm',
        'name': 'Stellar'
    },
    {
        'id': 'stratis',
        'symbol': 'strax',
        'name': 'Stratis'
    },
    {
        'id': 'streamcoin',
        'symbol': 'strm',
        'name': 'StreamCoin'
    },
    {
        'id': 'supercoin',
        'symbol': 'super',
        'name': 'SuperCoin'
    },
    {
        'id': 'syscoin',
        'symbol': 'sys',
        'name': 'Syscoin'
    },
    {
        'id': 'tagcoin',
        'symbol': 'tag',
        'name': 'Tagcoin'
    },
    {
        'id': 'tekcoin',
        'symbol': 'tek',
        'name': 'TEKcoin'
    },
    {
        'id': 'terracoin',
        'symbol': 'trc',
        'name': 'Terracoin'
    },
    {
        'id': 'trollcoin',
        'symbol': 'troll',
        'name': 'Trollcoin'
    },
    {
        'id': 'ufocoin',
        'symbol': 'ufo',
        'name': 'Uniform Fiscal Object'
    },
    {
        'id': 'unobtanium',
        'symbol': 'uno',
        'name': 'Unobtanium'
    },
    {
        'id': 'upcoin',
        'symbol': 'upcoin',
        'name': 'Upcoin'
    },
    {
        'id': 'vcash',
        'symbol': 'xvc',
        'name': 'Vcash'
    },
    {
        'id': 'verge',
        'symbol': 'xvg',
        'name': 'Verge'
    },
    {
        'id': 'vericoin',
        'symbol': 'vrc',
        'name': 'VeriCoin'
    },
    {
        'id': 'version',
        'symbol': 'v',
        'name': 'Version'
    },
    {
        'id': 'vertcoin',
        'symbol': 'vtc',
        'name': 'Vertcoin'
    },
    {
        'id': 'viacoin',
        'symbol': 'via',
        'name': 'Viacoin'
    },
    {
        'id': 'vpncoin',
        'symbol': 'vash',
        'name': 'VPNCoin'
    },
    {
        'id': 'waves',
        'symbol': 'waves',
        'name': 'Waves'
    },
    {
        'id': 'whitecoin',
        'symbol': 'xwc',
        'name': 'Whitecoin'
    },
    {
        'id': 'wolfcoin',
        'symbol': 'wolf',
        'name': 'WOLFCOIN'
    },
    {
        'id': 'woodcoin',
        'symbol': 'log',
        'name': 'Woodcoin'
    },
    {
        'id': 'worldcoin',
        'symbol': 'wdc',
        'name': 'WorldCoin'
    },
    {
        'id': 'yacoin',
        'symbol': 'yac',
        'name': 'YACoin'
    },
    {
        'id': 'yocoin',
        'symbol': 'yoc',
        'name': 'Yocoin'
    },
    {
        'id': 'zcash',
        'symbol': 'zec',
        'name': 'Zcash'
    },
    {
        'id': 'zeitcoin',
        'symbol': 'zeit',
        'name': 'Zeitcoin'
    },
    {
        'id': 'zetacoin',
        'symbol': 'zet',
        'name': 'Zetacoin'
    }
]


if __name__ == '__main__':
    new_image_dict = {}
    matched_shit = []
    remaining_coins_id = []
    remaining_coins_symbol = []

    for coin in coins:
        if coin['id'] in image_dict.keys():
            remaining_coins_id.append(coin)
            matched_shit.append(coin['id'])
    print(remaining_coins_id)
    print(len(remaining_coins_id))

    for coin in coins:
        if coin['id'] in image_dict.keys():
            new_image_dict[coin['id']] = image_dict[coin['id']]

    print(len(new_image_dict))
    print(new_image_dict)
