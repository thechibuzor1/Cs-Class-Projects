.data
.text 
	main: 
		li $s1,2
		li $s2,3
		li $s3,2
		li $s4,2
		
		bne $s3,$s4,Else
		add $s0,$s1,$s2
		j Exit
		
		Else: sub $s0,$s1,$s2
		Exit: 
	