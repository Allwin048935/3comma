# config.py
API_KEY = 'Hqod6Y5MDAkMmAJbRKOqUUDsYb9HG5aAkE3BMPZxHrm8JdZTgfIJr2RKSkRiOlDM'
API_SECRET = 'wVI5YTy9Y3dhiU1KoOSc0ysMVsAvaklSHDm40ZqkaHzKGgjlq9zlmi5CSF3n2wGw'
SECRET = 'eyJhbGciOiJIUzI1NiJ9.eyJzaWduYWxzX3NvdXJjZV9pZCI6MTAyNTR9.UpdSFm3FpcmR7hcVaBUOzPp5Q6-1gBRlQA21sH0ieHo'
THREE_COMMAS_WEBHOOK_URL = 'https://api.3commas.io/signal_bots/webhooks'
SELECTED_SYMBOLS = [
 '1INCH/USDT', 	'ARPA/USDT', 	'BIGTIME/USDT', 	'CHR/USDT', 	'DYDX/USDT', 	'FTM/USDT', 	'ID/USDT', 	'LINA/USDT', 	'MINA/USDT', 	'ONT/USDT', 	'REN/USDT', 	'STMX/USDT', 	'T/USDT', 	'XMR/USDT', 
'AAVE/USDT', 	'AAVE/USDT', 	'AR/USDT', 	'BLUR/USDT', 	'CHZ/USDT', 	'DYM/USDT', 	'FXS/USDT', 	'ILV/USDT', 	'LINK/USDT', 	'MKR/USDT', 	'OP/USDT', 	'REZ/USDT', 	'STORJ/USDT', 	'TWT/USDT', 	'XRP/USDT', 
'ACE/USDT', 	'ACE/USDT', 	'ASTR/USDT', 	'BLZ/USDT', 	'CKB/USDT', 	'EDU/USDT', 	'GALA/USDT', 	'IMX/USDT', 	'LISTA/USDT', 	'MOVR/USDT', 	'ORBS/USDT', 	'RIF/USDT', 	'STRK/USDT', 	'UMA/USDT', 	'XTZ/USDT', 
'ACH/USDT', 	'ACH/USDT', 	'ATA/USDT', 	'BNB/USDT', 	'COMBO/USDT', 	'EGLD/USDT', 	'GAS/USDT', 	'INJ/USDT', 	'LIT/USDT', 	'MTL/USDT', 	'PENDLE/USDT', 	'RLC/USDT', 	'STX/USDT', 	'UNFI/USDT', 	'XVS/USDT', 
'ADA/USDT', 	'ADA/USDT', 	'ATOM/USDT', 	'BNT/USDT', 	'COMP/USDT', 	'EIGEN/USDT', 	'GHST/USDT', 	'IOST/USDT', 	'LOKA/USDT', 	'MYRO/USDT', 	'PEOPLE/USDT', 	'RONIN/USDT', 	'SUI/USDT', 	'UNI/USDT', 	'YFI/USDT', 
'AERGO/USDT', 	'AERGO/USDT', 	'AUCTION/USDT', 	'BNX/USDT', 	'COS/USDT', 	'ENA/USDT', 	'GLM/USDT', 	'IOTA/USDT', 	'LOOM/USDT', 	'NEAR/USDT', 	'PERP/USDT', 	'ROSE/USDT', 	'SUN/USDT', 	'USDC/USDT', 	'YGG/USDT', 
'AEVO/USDT', 	'AEVO/USDT', 	'AVAX/USDT', 	'BOME/USDT', 	'COTI/USDT', 	'ENJ/USDT', 	'GMT/USDT', 	'IOTX/USDT', 	'LPT/USDT', 	'NEIRO/USDT', 	'PHB/USDT', 	'RPL/USDT', 	'SUPER/USDT', 	'USTC/USDT', 	
'ALGO/USDT', 	'ALGO/USDT', 	'AXL/USDT', 	'BOND/USDT', 	'CRV/USDT', 	'ENS/USDT', 	'GMX/USDT', 	'IO/USDT', 	'LQTY/USDT', 	'NEO/USDT', 	'PIXEL/USDT', 	'RSR/USDT', 	'SUSHI/USDT', 	'UXLINK/USDT', 	
'ALICE/USDT', 	'ALICE/USDT', 	'AXS/USDT', 	'BRETT/USDT', 	'CTSI/USDT', 	'EOS/USDT', 	'GRT/USDT', 	'JASMY/USDT', 	'LRC/USDT', 	'NFP/USDT', 	'POL/USDT', 	'RUNE/USDT', 	'SXP/USDT', 	'VANRY/USDT', 	
'ALPACA/USDT', 	'ALPACA/USDT', 	'BADGER/USDT', 	'BSV/USDT', 	'CYBER/USDT', 	'ETC/USDT', 	'GTC/USDT', 	'JOE/USDT', 	'LSK/USDT', 	'NKN/USDT', 	'POLYX/USDT', 	'RVN/USDT', 	'SYN/USDT', 	'VET/USDT', 	
'ALPHA/USDT', 	'ALPHA/USDT', 	'BAKE/USDT', 	'BSW/USDT', 	'DAR/USDT', 	'ETHFI/USDT', 	'G/USDT', 	'JTO/USDT', 	'LTC/USDT', 	'NMR/USDT', 	'POPCAT/USDT', 	'SAGA/USDT', 	'SYS/USDT', 	'VIDT/USDT', 	
'ALT/USDT', 	'ALT/USDT', 	'BAL/USDT', 	'BTCDOM/USDT', 	'DASH/USDT', 	'ETH/USDT', 	'HBAR/USDT', 	'KAS/USDT', 	'LUNA2/USDT', 	'NOT/USDT', 	'PORTAL/USDT', 	'SAND/USDT', 	'TAO/USDT', 	'VOXEL/USDT', 	'ZRO/USDT', 
'AMB/USDT', 	'AMB/USDT', 	'BANANA/USDT', 	'BTC/USDT', 	'DEFI/USDT', 	'ETHW/USDT', 	'HFT/USDT', 	'KAVA/USDT', 	'MAGIC/USDT', 	'NTRN/USDT', 	'POWR/USDT', 	'SFP/USDT', 	'THETA/USDT', 	'WAXP/USDT', 	'ZRX/USDT', 
'ANKR/USDT', 	'ANKR/USDT', 	'BAND/USDT', 	'C98/USDT', 	'DENT/USDT', 	'FET/USDT', 	'HIFI/USDT', 	'KDA/USDT', 	'MANA/USDT', 	'NULS/USDT', 	'QNT/USDT', 	'SKL/USDT', 	'TLM/USDT', 	'WIF/USDT', 	'ZEC/USDT', 
'APE/USDT', 	'APE/USDT', 	'BAT/USDT', 	'CAKE/USDT', 	'DIA/USDT', 	'FIDA/USDT', 	'HIGH/USDT', 	'KEY/USDT', 	'MASK/USDT', 	'OGN/USDT', 	'QTUM/USDT', 	'SNX/USDT', 	'TNSR/USDT', 	'WLD/USDT', 	'ZEN/USDT', 
'API3/USDT', 	'API3/USDT', 	'BB/USDT', 	'CATI/USDT', 	'DODOX/USDT', 	'FIL/USDT', 	'HMSTR/USDT', 	'KLAY/USDT', 	'MAVIA/USDT', 	'OMG/USDT', 	'QUICK/USDT', 	'SOL/USDT', 	'TOKEN/USDT', 	'WOO/USDT', 	'ZETA/USDT', 
'APT/USDT', 	'APT/USDT', 	'BCH/USDT', 	'CELO/USDT', 	'DOGE/USDT', 	'FIO/USDT', 	'HOOK/USDT', 	'KNC/USDT', 	'MAV/USDT', 	'OMNI/USDT', 	'RARE/USDT', 	'SPELL/USDT', 	'TRB/USDT', 	'W/USDT', 	'ZIL/USDT', 
'ARB/USDT', 	'ARB/USDT', 	'BEAMX/USDT', 	'CELR/USDT', 	'DOGS/USDT', 	'FLM/USDT', 	'HOT/USDT', 	'KSM/USDT', 	'MBOX/USDT', 	'OM/USDT', 	'REEF/USDT', 	'SSV/USDT', 	'TRU/USDT', 	'XAI/USDT', 	'ZK/USDT', 
'ARKM/USDT', 	'ARKM/USDT', 	'BEL/USDT', 	'CFX/USDT', 	'DOT/USDT', 	'FLOW/USDT', 	'ICP/USDT', 	'LDO/USDT', 	'METIS/USDT', 	'ONE/USDT', 	'REI/USDT', 	'STEEM/USDT', 	'TRX/USDT', 	'XEM/USDT', 	
'ARK/USDT', 	'ARK/USDT', 	'BICO/USDT', 	'CHESS/USDT', 	'DUSK/USDT', 	'FLUX/USDT', 	'ICX/USDT', 	'LEVER/USDT', 	'MEW/USDT', 	'ONG/USDT', 	'RENDER/USDT', 	'STG/USDT', 	'TURBO/USDT', 	'XLM/USDT'
]
