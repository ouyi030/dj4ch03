from django.db import models
class Post(models.Model):
    title =models.CharField(max_length=200) #文章標題
    slug=models.CharField(max_length=200)#連結本文章的網址
    body =models.TextField() #文章的內容
    pub_date = models.DateTimeField(auto_now_add=True)
#文章發表的時間。資料表中的記錄在建立時自動加入當時系統的時間


    class Meta: # 記錄的一些相關設定
        ordering = ('-pub_date',)
    #當記錄被取得時回傳的順序,前面加個減號代表我們想要傳回記錄時是以此欄位值(i.e.,文章發布時間)遞減的方式排序

#如果要顯示Post物件,就以文章標題顯示(在admin 管理介面或是shell 介面操作時,均會顯示標題欄位內容代表該記錄)
    def __str__(self):
        return self.title 


# Create your models here.
