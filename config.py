# config.py
API_KEY = 'Hqod6Y5MDAkMmAJbRKOqUUDsYb9HG5aAkE3BMPZxHrm8JdZTgfIJr2RKSkRiOlDM'
API_SECRET = 'wVI5YTy9Y3dhiU1KoOSc0ysMVsAvaklSHDm40ZqkaHzKGgjlq9zlmi5CSF3n2wGw'
SECRET = 'eyJhbGciOiJIUzI1NiJ9.eyJzaWduYWxzX3NvdXJjZV9pZCI6MTAyNTR9.UpdSFm3FpcmR7hcVaBUOzPp5Q6-1gBRlQA21sH0ieHo'
THREE_COMMAS_WEBHOOK_URL = 'https://api.3commas.io/signal_bots/webhooks'
SELECTED_SYMBOLS = [
    'BTC/USDT', 'ETH/USDT', 'BNB/USDT', 'BCC/USDT', 'NEO/USDT', 'LTC/USDT', 'QTUM/USDT', 'ADA/USDT', 'XRP/USDT', 'EOS/USDT', 'IOTA/USDT', 'XLM/USDT', 'ONT/USDT', 'TRX/USDT', 'ETC/USDT', 'ICX/USDT', 'VEN/USDT', 'NULS/USDT', 'VET/USDT', 'PAX/USDT', 'BCHABC/USDT', 'LINK/USDT',
 'WAVES/USDT', 'BTT/USDT', 'ONG/USDT', 'HOT/USDT', 'ZIL/USDT', 'ZRX/USDT', 'FET/USDT', 'BAT/USDT', 'XMR/USDT', 'ZEC/USDT', 'IOST/USDT', 'CELR/USDT', 'DASH/USDT', 'NANO/USDT', 'OMG/USDT', 'THETA/USDT', 'ENJ/USDT', 'MITH/USDT', 'MATIC/USDT', 'ATOM/USDT', 'TFUEL/USDT',
 'ONE/USDT', 'FTM/USDT', 'ALGO/USDT', 'GTO/USDT', 'ERD/USDT', 'DOGE/USDT', 'DUSK/USDT', 'ANKR/USDT', 'WIN/USDT', 'COS/USDT', 'NPXS/USDT', 'COCOS/USDT', 'MTL/USDT', 'TOMO/USDT', 'PERL/USDT', 'DENT/USDT', 'MFT/USDT', 'KEY/USDT', 'STORM/USDT', 'DOCK/USDT', 'WAN/USDT', 'FUN/USDT',
 'CVC/USDT', 'CHZ/USDT', 'BAND/USDT', 'BEAM/USDT', 'XTZ/USDT', 'REN/USDT', 'RVN/USDT', 'HC/USDT', 'HBAR/USDT', 'NKN/USDT', 'STX/USDT', 'KAVA/USDT', 'ARPA/USDT', 'IOTX/USDT', 'RLC/USDT', 'MCO/USDT', 'CTXC/USDT', 'BCH/USDT', 'TROY/USDT', 'VITE/USDT', 'FTT/USDT', 'OGN/USDT', 'DREP/USDT', 
'TCT/USDT', 'WRX/USDT', 'BTS/USDT', 'LSK/USDT', 'BNT/USDT', 'LTO/USDT', 'STRAT/USDT', 'AION/USDT', 'MBL/USDT', 'COTI/USDT', 'STPT/USDT', 'WTC/USDT', 'DATA/USDT', 'XZC/USDT', 'SOL/USDT', 'CTSI/USDT', 'HIVE/USDT', 'CHR/USDT', 'GXS/USDT',
 'ARDR/USDT', 'LEND/USDT', 'MDT/USDT', 'STMX/USDT', 'KNC/USDT', 'REP/USDT', 'LRC/USDT', 'PNT/USDT', 'COMP/USDT', 'BKRW/USDT', 'SC/USDT', 'ZEN/USDT', 'SNX/USDT', 'VTHO/USDT', 'DGB/USDT', 'SXP/USDT', 'GBP/USDT', 'MKR/USDT', 'DAI/USDT', 'DCR/USDT', 'MANA/USDT', 'AUD/USDT', 
'YFI/USDT', 'BAL/USDT', 'BLZ/USDT', 'IRIS/USDT', 'KMD/USDT', 'JST/USDT', 'SRM/USDT', 'ANT/USDT', 'CRV/USDT', 'SAND/USDT', 'OCEAN/USDT', 'NMR/USDT', 'DOT/USDT', 'LUNA/USDT', 'RSR/USDT', 'PAXG/USDT', 'WNXM/USDT', 'TRB/USDT', 'BZRX/USDT', 
'YFII/USDT', 'KSM/USDT', 'EGLD/USDT', 'DIA/USDT', 'RUNE/USDT', 'FIO/USDT', 'UMA/USDT', 'BEL/USDT', 'WING/USDT', 'UNI/USDT', 'NBS/USDT', 'OXT/USDT', 'SUN/USDT', 'AVAX/USDT', 'HNT/USDT', 'FLM/USDT', 'ORN/USDT', 'UTK/USDT', 'XVS/USDT', 'ALPHA/USDT', 'AAVE/USDT', 'NEAR/USDT',
 'FIL/USDT', 'INJ/USDT', 'AUDIO/USDT', 'CTK/USDT', 'AKRO/USDT', 'AXS/USDT', 'HARD/USDT', 'DNT/USDT', 'STRAX/USDT', 'UNFI/USDT', 'ROSE/USDT', 'AVA/USDT', 'SKL/USDT', 'GRT/USDT', 'JUV/USDT', 'PSG/USDT', '1INCH/USDT', 'REEF/USDT', 'OG/USDT', 
'ATM/USDT', 'ASR/USDT', 'CELO/USDT', 'RIF/USDT', 'TRU/USDT', 'CKB/USDT', 'TWT/USDT', 'FIRO/USDT', 'LIT/USDT', 'SFP/USDT', 'DODO/USDT', 'CAKE/USDT', 'ACM/USDT', 'BADGER/USDT', 'FIS/USDT', 'OM/USDT', 'POND/USDT', 'DEGO/USDT', 'ALICE/USDT', 'LINA/USDT', 'PERP/USDT', 'RAMP/USDT',
 'SUPER/USDT', 'CFX/USDT', 'EPS/USDT', 'AUTO/USDT', 'TKO/USDT', 'PUNDIX/USDT', 'TLM/USDT', 'BTG/USDT', 'MIR/USDT', 'BAR/USDT', 'FORTH/USDT', 'BAKE/USDT', 'BURGER/USDT', 'SLP/USDT', 'SHIB/USDT', 'ICP/USDT', 'AR/USDT', 'POLS/USDT', 'MDX/USDT', 'MASK/USDT', 'LPT/USDT', 'NU/USDT', 'XVG/USDT',
 'ATA/USDT', 'GTC/USDT', 'TORN/USDT', 'KEEP/USDT', 'ERN/USDT', 'KLAY/USDT', 'PHA/USDT', 'MLN/USDT', 'DEXE/USDT', 'C98/USDT', 'CLV/USDT', 'QNT/USDT', 'FLOW/USDT', 'TVK/USDT', 'MINA/USDT', 'RAY/USDT', 'FARM/USDT', 'ALPACA/USDT',
 'QUICK/USDT', 'MBOX/USDT', 'FOR/USDT', 'REQ/USDT', 'GHST/USDT', 'WAXP/USDT', 'TRIBE/USDT', 'GNO/USDT', 'XEC/USDT', 'ELF/USDT', 'DYDX/USDT', 'POLY/USDT', 'VIDT/USDT', 'GALA/USDT', 'ILV/USDT', 'YGG/USDT', 'SYS/USDT', 'DF/USDT', 'FIDA/USDT', 'FRONT/USDT', 'CVP/USDT', 'AGLD/USDT', 
'RAD/USDT', 'BETA/USDT', 'RARE/USDT', 'LAZIO/USDT', 'CHESS/USDT', 'ADX/USDT', 'AUCTION/USDT', 'DAR/USDT', 'BNX/USDT', 'RGT/USDT', 'MOVR/USDT', 'CITY/USDT', 'ENS/USDT', 'QI/USDT', 'PORTO/USDT', 'POWR/USDT', 'VGX/USDT',
 'JASMY/USDT', 'AMP/USDT', 'PLA/USDT', 'PYR/USDT', 'RNDR/USDT', 'ALCX/USDT', 'SANTOS/USDT', 'MC/USDT', 'ANY/USDT', 'BICO/USDT', 'FLUX/USDT', 'FXS/USDT', 'VOXEL/USDT', 'HIGH/USDT', 'CVX/USDT', 'PEOPLE/USDT', 'OOKI/USDT', 'SPELL/USDT',
 'JOE/USDT', 'ACH/USDT', 'IMX/USDT', 'GLMR/USDT', 'LOKA/USDT', 'SCRT/USDT', 'API3/USDT', 'BTTC/USDT', 'ACA/USDT', 'ANC/USDT', 'XNO/USDT', 'WOO/USDT', 'ALPINE/USDT', 'ASTR/USDT', 'GMT/USDT', 'KDA/USDT', 'APE/USDT', 'BSW/USDT', 'BIFI/USDT', 'MULTI/USDT', 'STEEM/USDT', 'MOB/USDT', 
'NEXO/USDT', 'REI/USDT', 'GAL/USDT', 'LDO/USDT', 'EPX/USDT', 'OP/USDT', 'LEVER/USDT', 'STG/USDT'
]
