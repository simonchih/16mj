# 翡翠麻將美術

所有原有 60 張 GIF 已以同名 PNG 重製，另加 icon.png；Image 共 61 張圖。
規則／AI／計台延續原遊戲。原始棋盤座標與 44×53 牌面尺寸保留。
象牙白面、深綠玉質牌背、金色鑲邊、朱紅／墨綠／靛藍符號。
牌面由 tools/build_art.py 用 Pygame 向量繪圖與內附中文字型建置，
以四倍解析度抗鋸齒，確保數字、字牌與筒索數量正確。
碰顯示三張同牌；槓在原副露格內並排四張略縮小的牌，四個方位一致。

## 桌面生成

使用內建 image_gen 工具，無 API／CLI。原圖：art/table-source.png。
正式遊戲載入 Image/Nostalgy.png（1200×900）。

完整 prompt：

Use case: stylized-concept. Asset type: actual background texture for a 1200x900 top-down Taiwanese mahjong Pygame game. Create a luxurious emerald green velvet mahjong table viewed EXACTLY overhead, rectangular 4:3 landscape image. Rounded polished metallic gold rim ONLY at very outer edge (outermost 2 percent), subtle gold cloud engravings in corners and very faint bamboo foliage at upper right edge. Rich deep jade felt with subtle fine grain, soft lighting with slightly brighter center. Entire center 90 percent is clear even dark green playing surface, ample empty space for cards rendered by code. NO tiles, NO objects, NO lettering, NO logos, NO watermark, NO perspective. Match the user's reference aesthetic of polished gold, rich emerald green and luxurious traditional Chinese mahjong.

## 重新建置

執行 `.venv\Scripts\python.exe tools\build_art.py`。
只重建圖片，不修改遊戲程式。桌面原稿須保留。

## 特效

jade_ui.py 負責金色粒子、擴散光圈、摸牌／落牌提示、吃碰槓補花字幕、
聽牌提示與胡牌慶祝。效果以實際時間更新，不修改遊戲亂數與判定。
等待期間持續處理關閉視窗；渲染限速 60 FPS，字型與旋轉素材快取。
