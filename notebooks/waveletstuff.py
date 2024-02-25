titles = ['Approximation', ' Horizontal detail',
          'Vertical detail', 'Diagonal detail']
coeffs2 = pywt.dwt2(train_image_arr[0], 'bior1.3')
LL, (LH, HL, HH) = coeffs2

fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1,5,1)
ax2 = fig.add_subplot(1,5,2)
ax3 = fig.add_subplot(1,5,3)
ax4 = fig.add_subplot(1,5,4)
ax5 = fig.add_subplot(1,5,5)

ax1.imshow(train_image_arr[0])
ax1.set_title("Original")
ax2.imshow(LL, interpolation="nearest") 
ax2.set_title("Approximation")
ax3.imshow(LH, interpolation="nearest") 
ax3.set_title("Horizontal detail")
ax4.imshow(HL, interpolation="nearest") 
ax4.set_title("Vertical detail")
ax5.imshow(HH, interpolation="nearest") 
ax5.set_title("Diagonal detail")
plt.show()