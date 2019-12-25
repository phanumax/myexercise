lv_rao = int(input('คุณเลเวล: '))
if(lv_rao<1 or lv_rao>100):
    print('เลเวลผู้เล่นต้องอยู่ระหว่าง 1 ถึง 100')
else:
    lv_sattru = int(input('ศัตรูเลเวล: '))
    if(lv_sattru<1 or lv_sattru>500):
        print('เลเวลศัตรูต้องอยู่ระหว่าง 1 ถึง 500')
    else:
        if(lv_rao+50<=lv_sattru):
            print('ศัตรูเมพเกินไป')
        elif(lv_rao-50>=lv_sattru):
            print('ศัตรูกากเกินไป')
        else:
            print('คุณมีโอกาสชนะ', 50+lv_rao-lv_sattru,'%')
