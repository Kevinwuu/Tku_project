# 大三專題
**自動違規取締系統**
	主要先做違規取締部分，路況或車輛追蹤之類以後再擴充。
    - 紅燈右轉
    - 兩段式左轉
    - 車速
    - 闖紅燈(超過停止線)
    - sgredesgs

## 分組個別實作
- 紅綠燈燈號辨識
- 車子抓取
- 車子辨識

### 車輛辨識方法

- #### 背景相減法
-
    濾除背景效果很好，
    但如果都用同一張frame當背景，在晚上時相減效果會很不好。

- #### connected component

    結果還是要先做背景相減後才可以得到比較乾淨的圖像，只要邊緣有斷掉label就會斷掉。
    只能分辨出不同的車輛並且隨機上色，但無法知道下張frame同個物件為哪個。

- #### canny邊緣偵測

    邊緣線段太多反而不好找出整塊車體。

    (X)
- #### ML

    需要大量資料來訓練。

- #### 混合高斯模型(MGM)

    opencv提供三種backgrooundsubstractor 方法來實踐前景去除

    MOG, MOG2, KNN。

### 車輛追蹤

- HOG特徵

    只要車輛角度一改變就完全是不同的物體了。

    不過每個frAme之間會改變的角度應該不大 ( ?

- 色彩histogram

    兩台車顏色太像可能會有問題。

- 移動距離

    可能判斷成隔壁車道靠很近的車

- 方向&角度

    在同個方向向量上轉動角度在一定範圍內就是同台車。

### 場景架設


### 參考資料
[網路資源](http://beta.hackfoldr.org/kevinisme/https%253A%252F%252Fhackmd.io%252FKYFg7ArADDBGC0UBMYCc8SwGxXgQwEYATAZngOADMoAOMPWE1FIA%253Fview)


[專題討論紀錄](http://beta.hackfoldr.org/kevinisme/https%253A%252F%252Fhackmd.io%252FKYFg7ArADDBGC0UBMYCc8SwGxXgQwEYATAZngOADMoAOMPWE1FIA%253Fview)
