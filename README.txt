== 翡翠美術重製版 ==

本機直接雙擊 Start-Mahjong.cmd 啟動（已建立 .venv）。
其他電腦建議 Python 3.10+，在專案目錄執行：
  py -3 -m venv .venv
  .venv\Scripts\python.exe -m pip install -r requirements.txt
  .venv\Scripts\python.exe p16mj.py

美術：Image 下全部 60 張舊 GIF 已替換為 PNG，新增一張視窗圖示。
翡翠桌面、象牙牌面、金框、牌背、風位與按鈕全面重製。
新增落牌／摸牌光圈、金色粒子、吃碰槓補花提示及胡牌動畫。
碰為 3 張相同牌；槓為 4 張相同牌，在同一副露格略縮小並排。
既有台灣十六張流程、AI、聽牌與計台維持原設計。
注意：選中按鈕現為金色外框與金字（下方舊說明的「紅字」）。

驗證：
  .venv\Scripts\python.exe -m unittest discover -s tests -v
  .venv\Scripts\python.exe tools\smoke_game.py --rounds 12
  .venv\Scripts\python.exe tools\smoke_game.py --native --rounds 3 --seed 42

美術原稿、完整生成提示及重建方式：art/ART_DIRECTION.md。
執行遊戲不需 Pillow 或 imagegen；僅需 requirements.txt 中的 pygame-ce。
16mj.spec 已更新主程式路徑與圖片／字型打包清單；未在本次驗證中建置 EXE。

下方為原版規則說明；Image source 為舊版素材歷史來源。
Image source:
Mahjong wiki(https://en.wikipedia.org/wiki/Mahjong)
TJMJ(https://sourceforge.net/projects/tjmj/)
http://163.20.160.14/~word/modules/myalbum_search/

==Environment==
Python 3.6 and Pygame

Chinese readme below.

==遊戲說明==
大部份採用台灣16張麻將的規則，一開始隨機選出一家做東家，
由東家開始做莊，電腦會避免吃6萬打6萬，
或者手牌有5, 6萬吃7萬，打4萬之類的，
但是人類玩家仍然可以這樣吃。

* 當"碰"發生時，玩家可以按"碰"的按鈕，會自動處理碰。

* 當"吃"發生時，玩家可以按"吃"的按鈕，按鈕會變紅字，
此時用滑鼠鍵選兩張手牌，如果可以吃，會自動處理。
(即使只有一組可吃，也需要玩家選牌)

* 當"吃"和"碰"(槓))都發生時，會先顯示碰(槓)，
玩家如要執行"吃"，需先按"返"，才會出現"吃"的按鈕。

* 當"碰槓"發生時，玩家可以按"槓"的按鈕，會自動處理碰槓。

* 當"暗槓"發生時，玩家可以按"槓"的按鈕，按鈕會變紅字，
此時用滑鼠選手牌，當手牌有四張一樣，或有三張手牌一樣，
且摸到的牌也跟這三張一樣，會自動處理暗槓。
(即使只有一組可暗槓，也需要玩家選牌)

* 當"加槓"發生時，玩家可以按"槓"的按鈕，按鈕會變紅字，
此時用滑鼠選碰牌，當玩家手牌或摸到的牌中有跟碰牌一樣的，
會自動處理加槓。
(即使只有一組可加槓，也需要玩家選牌)

* 當"聽"發生時，玩家可以按"聽"的按鈕，聽的按鈕會變紅字，
且會自動進入聽的模式。在聽的模式下，如果可以暗槓，
且暗槓之後仍然聽牌，會自動暗槓。否則不能胡牌的話，
會自動丟牌。另外聽牌在台灣麻將規則中，不一定要說，
通常是不說，所以電腦不會告知自己聽牌，除非是天聽或地聽。

* 當"胡"牌發生時，可以按"胡"的按鈕，宣告自己胡牌。

* 當按下"返"的按鈕時，如果有聽以外的按鈕是紅字，
會將按鈕回復到不是紅字。否則，會放棄吃，碰，槓或胡牌。

* 除了聽的紅字按鈕以外，當按下按鈕變紅字時，再按一次該按鈕，
可以回復成黑字的狀態。
