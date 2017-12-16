# Tku_project
Tku專題(自動違規取締系統)
	主要先做違規部分，路況或車輛追蹤之類以後再擴充。

## 分組個別實作
- 紅綠燈燈號辨識
- 車子抓取
- 車子辨識

### 車輛辨識
- #### 背景相減法
    濾除背景效果很好，
    但如果都用同一張frame當背景，在晚上時相減效果會很不好。

- #### connected component
    結果還是要先做背景相減後才可以得到比較乾淨的圖像，只要邊緣有斷掉label就會斷掉。
    只能分辨出不同的車輛並且隨機上色，但無法知道下張frame同個物件為哪個。

- #### canny邊緣偵測
    邊緣線段太多反而不好找出整塊車體。
    (X)

### 車輛追蹤

- HOG特徵
    只要車輛角度一改變就完全是不同的物體了。
- 色彩histogram
    

### 參考資料
[網路資源](http://beta.hackfoldr.org/kevinisme/https%253A%252F%252Fhackmd.io%252FKYFg7ArADDBGC0UBMYCc8SwGxXgQwEYATAZngOADMoAOMPWE1FIA%253Fview)
[專題討論紀錄](http://beta.hackfoldr.org/kevinisme/https%253A%252F%252Fhackmd.io%252FKYFg7ArADDBGC0UBMYCc8SwGxXgQwEYATAZngOADMoAOMPWE1FIA%253Fview)
