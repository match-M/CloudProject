function DateDiff(sDate1,sDate2){ //sDate1和sDate2是2002-12-18格式
       var  aDate,  oDate1,  oDate2,  iDays;
       aDate  =  sDate1.split("-");
       oDate1  =  new  Date(aDate[1]  +  '-'  +  aDate[2]  +  '-'  +  aDate[0]);    //转换为12-18-2002格式
       aDate  =  sDate2.split("-");
       oDate2  =  new  Date(aDate[1]  +  '-'  +  aDate[2]  +  '-'  +  aDate[0]);
       iDays  =  parseInt(Math.abs(oDate1  -  oDate2)  /  1000  /  60  /  60  /24);   //把相差的毫秒数转换为天数
       return  iDays;
}
const date = new Date();
const year = date.getFullYear();
const today = date.getDate();
const Month = date.getMonth() + 1;
var startTiem = "2019-9-1";
var overTime = year +"-"+ Month +"-"+ today;
document.write("我们在一起已经："+DateDiff(startTiem,overTime)+"天啦！");