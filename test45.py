import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans


def make_matrix(tab1, tab2):
  
    tmp2 = []
    
    for i in range(1, len(tab1)):
        tmp2.append([tab1[i], tab2[i]])
        
    tmp1 = np.array(tmp2)
    return tmp1


# rpeak
Y = [537212.00, 200794.88, 125712.00, 125435.90, 79215.00, 100678.66, 70980.00, 51720.76, 38745.91, 55423.56, 29354.00, 27154.30, 41461.15, 32576.63, 26873.86, 25159.68, 23047.20, 25025.81, 19464.20, 27880.65, 25705.90, 24913.46, 18621.14, 23396.35, 18309.22, 11209.11, 15142.20, 15208.23, 11032.03, 10321.92, 12127.07, 13977.60, 10510.66, 10469.38, 12902.40, 9492.16, 8128.51, 12039.37, 11661.31, 8789.76, 7785.68, 10296.12, 7455.92, 9891.07, 8439.62, 7107.15, 8911.26, 9220.61, 9125.22, 9125.22, 9793.54, 7235.17, 8316.52, 7060.68, 7630.85, 6712.32, 6981.48, 7519.30, 7257.60, 5332.32, 6193.15, 5267.14, 6912.00, 7345.56, 8848.49, 6134.17, 7136.87, 6618.93, 6628.15, 5783.81, 4718.59, 6635.52, 5369.86, 4249.33, 4249.33, 6563.84, 4006.20, 5365.09, 6023.99, 5419.01, 5750.78, 6253.06, 6131.84, 6131.84, 5879.81, 6844.80, 5120.00, 6412.03, 5834.40, 4570.56, 4896.51, 4896.51, 3791.58, 4592.64, 4777.57, 4605.00, 5371.78, 5014.73, 3481.06, 4352.41, 4881.25, 5610.48, 6080.00, 4608.00, 4971.11, 4884.48, 5483.52, 4867.20, 3962.88, 5888.00, 4335.21, 5760.00, 4709.38, 6327.55, 3670.43, 3578.27, 3019.16, 3019.16, 4190.21, 5440.00, 5376.00, 5312.00, 5354.88, 3761.66, 3894.91, 5312.00, 5248.00, 4085.76, 4219.09, 5184.00, 5529.60, 4710.40, 4829.34, 3207.86, 3207.86, 5120.00, 4354.56, 4895.54, 4085.76, 4359.98, 3798.60, 4992.00, 5145.60, 2808.69, 4701.00, 3847.22, 4229.85, 3388.03, 3570.28, 4915.20, 3682.36, 4112.64, 3299.33, 4680.00, 4680.00, 4946.79, 4800.00, 2601.98, 4004.25, 4736.00, 4239.36, 4704.00, 4180.48, 2895.36, 2895.36, 4640.00, 4684.80, 3686.40, 4121.60, 2812.80, 10321.92, 4368.00, 4368.00, 4480.00, 4480.00, 4480.00, 3581.76, 4480.00, 4412.10, 4003.84, 4354.56, 2867.41, 4890.00, 4368.00, 4368.00, 4368.00, 4368.00, 7494.78, 3923.71, 3905.28, 2688.00, 3041.28, 4320.00, 4515.84, 4816.00, 2534.40, 4160.00, 4423.68, 4423.68, 4423.68, 2585.09, 4300.80, 8973.31, 4406.89, 7112.70, 4056.00, 4056.00, 4056.00, 4056.00, 3903.43, 4652.03, 3434.09, 4000.00, 3072.00, 2846.40, 3843.38, 4225.20, 4225.20, 4225.20, 2984.45, 5245.78, 4018.18, 3074.53, 3862.25, 3936.00, 4648.18, 4648.18, 3840.00, 4080.38, 44982.27, 3840.00, 3744.00, 3744.00, 8160.77, 3693.54, 2985.98, 2985.98, 3053.57, 2359.30, 4104.32, 39936.00, 3776.00, 3052.34, 4096.51, 4096.51, 4085.76, 6594.56, 4010.48, 4010.48, 4010.48, 2800.87, 2491.37, 3603.46, 3960.32, 3921.41, 3905.13, 2409.60, 4618.00, 3974.40, 3981.31, 3520.51, 3660.80, 4292.35, 3179.52, 3843.84, 2193.01, 3816.96, 3612.67, 15162.37, 3520.51, 2586.01, 2801.41, 3520.00, 4080.05, 3432.00, 2727.03, 2687.39, 3698.69, 6123.52, 3686.40, 2298.24, 7436.80, 3456.00, 4329.73, 4981.76, 3353.18, 3669.12, 4140.03, 4140.03, 3644.93, 2674.10, 3021.60, 3021.60, 3698.69, 2923.78, 2438.14, 3696.00, 3072.77, 2861.57, 5888.00, 7312.90, 2672.64, 2709.50, 2568.19, 81410.56, 7206.91, 2799.36, 3072.00, 3072.00, 3072.00, 3978.24, 3440.64, 2816.00, 3149.60, 2688.00, 2737.15, 2304.00, 2703.36, 2488.32, 2703.36, 2695.68, 3446.78, 3290.11, 2348.64, 2674.94, 3207.17, 2472.96, 2467.70, 3440.64, 3137.87, 2759.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 2119.68, 3520.51, 2649.29, 3788.80, 3766.37, 3766.37, 2550.53, 3072.00, 2036.74, 2036.74, 3715.89, 2637.71, 1904.64, 3008.00, 2323.28, 3333.12, 2580.48, 2573.38, 3225.60, 1931.63, 2399.74, 2944.00, 6535.68, 3238.40, 2987.52, 2987.52, 2987.52, 2509.04, 2985.98, 2880.00, 3225.60, 3182.59, 1792.63, 2816.00, 2444.71, 2987.52, 2412.54, 2752.00, 3053.57, 3931.20, 3000.00, 1739.78, 2688.00, 2011.64, 2316.04, 2316.04, 2153.54, 5772.80, 2624.00, 1677.72, 1920.00, 2413.82, 2914.56, 1999.87, 1530.55, 3907.58, 2890.24, 2226.56, 5793.79, 5740.80, 3553.18, 2329.60, 3068.93, 2560.00, 4917.66, 2953.60, 2459.00, 2903.04, 1676.51, 1836.17, 1667.17, 2073.60, 2332.00, 2780.47, 2457.60, 3489.02, 2770.94, 1920.00, 2863.41, 2027.52, 2088.96, 2400.00, 2400.00, 2393.60]
# cores
X = [7630848, 2414592, 1572480, 10649600, 555520, 4981760, 449280, 669760, 448448, 672520, 347776, 387872, 979072, 391680, 305856, 698880, 288288, 291024, 276480, 622336, 570020, 556104, 253600, 561408, 367024, 127488, 204032, 170352, 130000, 294912, 135828, 174720, 34560, 294912, 169920, 107568, 241920, 197120, 280320, 99600, 110592, 153216, 211816, 114480, 100096, 241108, 120296, 99792, 135792, 135792, 127520, 196608, 124416, 169728, 103680, 220800, 88400, 79560, 75600, 144900, 172032, 41664, 72000, 93960, 91936, 163840, 81600, 76608, 71424, 70416, 131072, 79488, 145920, 126468, 126468, 155150, 119232, 65208, 85568, 70560, 86400, 80640, 72800, 72800, 63360, 85560, 215040, 38400, 67584, 124200, 60512, 60512, 113832, 62400, 55296, 72000, 60480, 71232, 110160, 59136, 225984, 152692, 76000, 128000, 53568, 63840, 122400, 61120, 99072, 73600, 64512, 72000, 49056, 94160, 79104, 86016, 89856, 89856, 54560, 68000, 67200, 66400, 59976, 37920, 52920, 66400, 65600, 53200, 47808, 64800, 69120, 128000, 43200, 95472, 95472, 64000, 50400, 67584, 53200, 14848, 66000, 62400, 64320, 83592, 186368, 23040, 50816, 194616, 85824, 61440, 100064, 61200, 91648, 50400, 50400, 64384, 60000, 73920, 48128, 59200, 115200, 58800, 113600, 69600, 69600, 58000, 58560, 46080, 112000, 19840, 153600, 48160, 48160, 53760, 53760, 53760, 53300, 56000, 49920, 108800, 50400, 37440, 55104, 47320, 47320, 47320, 47320, 72480, 40560, 40800, 50176, 76032, 54000, 67200, 50400, 72000, 52000, 49800, 49800, 49800, 73440, 128000, 121920, 94976, 96640, 44200, 44720, 44720, 44720, 44720, 53760, 40960, 50000, 40000, 166304, 44032, 48160, 48160, 48160, 32160, 59760, 52320, 174720, 44160, 49200, 53040, 53040, 48000, 55440, 48880, 48000, 41280, 40800, 110880, 42312, 34560, 34560, 39760, 36864, 116600, 520000, 47200, 41472, 121920, 121920, 60800, 89600, 45152, 45152, 45152, 49432, 66304, 41280, 47600, 53280, 58112, 60240, 51504, 54000, 41472, 40320, 57200, 49680, 86400, 46200, 65268, 56800, 47040, 173680, 40320, 70272, 28240, 44000, 46480, 37440, 33856, 31104, 55040, 83200, 48000, 143640, 116200, 43200, 80640, 66080, 41760, 44100, 48880, 48880, 54240, 30600, 36000, 36000, 110080, 33840, 67456, 105000, 38552, 33120, 80000, 99360, 34800, 35280, 145920, 2312800, 97920, 32400, 38400, 38400, 38400, 118400, 38400, 35200, 39680, 40000, 31680, 57600, 35200, 32400, 35200, 28800, 97920, 48960, 55728, 30960, 41760, 100800, 31524, 89600, 1664, 78400, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 57600, 40320, 37632, 43520, 42752, 42752, 118080, 38400, 48960, 48960, 55296, 32144, 59520, 37600, 27768, 86800, 33600, 31360, 48000, 62944, 27520, 36800, 88800, 92000, 34400, 34400, 34400, 30576, 38880, 36000, 84000, 82880, 53352, 35200, 29792, 34400, 29400, 34400, 79520, 42840, 33000, 23040, 33600, 76896, 28224, 28224, 26180, 82000, 32800, 131072, 48000, 30240, 82800, 52080, 73584, 46080, 33600, 25232, 78720, 78000, 44016, 28000, 32640, 32000, 59392, 34000, 30624, 43200, 49896, 54648, 77184, 25920, 31680, 82752, 32000, 40320, 78720, 24000, 35712, 26400, 27200, 30000, 30000, 29920]


tab = make_matrix(X, Y)


plt.scatter(tab[:,0],tab[:,1], label='True Position')
kmeans = KMeans(n_clusters=3)
kmeans.fit(tab)
#les nouvelles valeurs de centroïde
print("les coordonnées des centroïdes")
print( kmeans.cluster_centers_)
plt.scatter(tab[:,0],tab[:,1], c=kmeans.labels_, cmap='rainbow')

##coloration des centroïdes de chaque cluster 
plt.scatter(tab[:,0], tab[:,1], c=kmeans.labels_, cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], color='black')
plt.title('clustering centroide avec le k-Means')

plt.show()
plt.savefig("45.png", bbox_inches = "tight")