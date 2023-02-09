import random
exit_loop = False
exit_loop2 = False
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
smile = 0
humen = 0
listsmile = ["ดีมากที่สุด", "ดีมาก", "พอใช้", "น้อย"]
# ฐานข้อมูลATOM
hi = ['Hi', 'Hello', 'สวัสดีครับ', 'สวัสดีค่ะ', 'สวัสดี']
hibot = ['คุณลูกค้าชื่ออะไรหรอครับ ?', 'คุณชื่ออะไรหรอครับ ???']
yes = ['ได้ครับ', 'ครับ', 'ได้ค่ะ', 'Yes', 'ค่ะ', 'ได้', 'ก็ได้']
yesbot = ['ขอบคุณครับ']
no = ['ไม่ได้ครับ', 'ไม่', 'ไม่ได้ค่ะ', 'No', 'ไม่ได้', 'no']
nobot = ['ช่วยเค้าหน่อยน้าาา !!!!!', 'ช่วยผมหน่อยน้าค๊าบบบ']
smile_verygood = ['ดีมากที่สุด']
smile_verygood_bot = ['เย้เย้~ ~ ',
                      'ขอบคุค๊าบบบบบบบบ', 'VeryGooooooddddd ', 'Wow']
smile_good = ['ดีมาก']
smile_good_bot = ['ขอบคุณครับ', 'ดีใจจัง']
smile_well = ['พอใช้']
smile_well_bot = ['จะพยามพัฒนาต่อไปครับ', 'ขอบคุณครับ']
smile_bad = ['น้อย']
smile_bad_bot = ['จะรีบปรับปรุงให้ดีที่สุดครับ', 'ขอโทษด้วยครับ']
# ประเมินความพึงพอใจ


def start_admin():
    print("\tกรุณาใส่รหัสผ่าน")
    user_admin = input("User : ")
    pass_admin = int(input("Pass : "))
    if user_admin == 'admin' and pass_admin == 123456789:
        print("\t\t\twellcome to admin ")
        if (800 < smile <= 1000):
            print(
                "-------------------------------------------------------------------------------")
            for var in listsmile:
                print(end="\t\t")
                print(var, end="")
            print("")
            print(
                "คะแนน         10                     8                        6                  4")
            print("รวมคะแนน    {}                       {}                      {}                  {}".format(
                sum1, sum2, sum3, sum4))
            print("")
            print("จำนวนคนที่ประเมิณ {}                         ทั้งหมด {} คะแนน".format(
                humen, smile))
            print("ร้านอยู่ในเกณฑ์      เยี่ยมมาก")
            print(
                "-------------------------------------------------------------------------------")
        elif (600 <= smile < 800):
            print(
                "-------------------------------------------------------------------------------")
            for var in listsmile:
                print(end="\t\t")
                print(var, end="")
            print("")
            print(
                "คะแนน         10                     8                        6                  4")
            print("รวมคะแนน    {}                       {}                      {}                  {}".format(
                sum1, sum2, sum3, sum4))
            print("")
            print("จำนวนคนที่ประเมิณ {}                         ทั้งหมด {} คะแนน".format(
                humen, smile))
            print("ร้านอยู่ในเกณฑ์      มาตราฐาน")
            print(
                "-------------------------------------------------------------------------------")
        elif (400 <= smile < 600):
            print(
                "-------------------------------------------------------------------------------")
            for var in listsmile:
                print(end="\t\t")
                print(var, end="")
            print("")
            print(
                "คะแนน         10                     8                        6                  4")
            print("รวมคะแนน    {}                       {}                      {}                  {}".format(
                sum1, sum2, sum3, sum4))
            print("")
            print("จำนวนคนที่ประเมิณ {}                         ทั้งหมด {} คะแนน".format(
                humen, smile))
            print("ร้านอยู่ในเกณฑ์      พอใช้")
            print(
                "-------------------------------------------------------------------------------")
        elif (0 <= smile < 400):
            print(
                "-------------------------------------------------------------------------------")
            for var in listsmile:
                print(end="\t\t")
                print(var, end="")
            print("")
            print(
                "คะแนน         10                     8                        6                  4")
            print("รวมคะแนน    {}                       {}                      {}                  {}".format(
                sum1, sum2, sum3, sum4))
            print("")
            print("จำนวนคนที่ประเมิณ {}                         ทั้งหมด {} คะแนน".format(
                humen, smile))
            print("ร้านอยู่ในเกณฑ์      ควรปรับปรุง")
            print(
                "-------------------------------------------------------------------------------")
    else:
        print("*****************************************")
        print("รหัสผ่านผิด")
        print("*****************************************")


###################################
while True:
    exit_loop2 = False
    print("โปรแกรมประเมินความพึงพอใจลูกค้า")
    print("1.เริ่มการทำงาน \t2.ประเมิณแบบสอบถาม  \t3.รีเซ็ตคะแนน  \t4.ออกจากระบบ")
    start = int(input(">"))
    print("----------------------------------------------------------")
####################################
    if start == 1:
        for i in range(1, 101):
            exit_loop = False
            while True:
                print("1.ทำแบบสอบถาม \t2.ออกจากแบบสอบถาม")
                start_loop = int(input(" "))
                if start_loop == 1:
                    break
                elif start_loop == 2:
                    exit_loop2 = True
                    break
                else:
                    print("----------------------------------------------------------")
                    print("เลือกคำสั่ง 1 หรือ 2 ครับ")
                    print("----------------------------------------------------------")
            if exit_loop2 == True:
                break
            print("----------------------------------------------------------")
            print("atom : สวัสดีครับ ~~")
            while True:
                text = input("> ")
                if text in hi:
                    print("atom : ผมชื่อ ATOM")
                    print("atom : ", random.choice(hibot))
                    name_user = input("> ")
                    print(
                        "atom : คุณ{} ช่วยทำแบบประเมิณให้ผมหน่อยได้ไหมครับ".format(name_user))
                elif text in yes:
                    print("atom :", random.choice(yesbot))
                    print(
                        "atom : กรุณาตอบ \"ดีมากที่สุด\" \"ดีมาก\" \"พอใช้\" \"น้อย\'' ")
                    for i in range(1, 6):
                        if i == 1:
                            print("atom : คุณ{} คิดว่าบริการทางการเงินด้านเงินฝากของเราเป็นอย่างไร ? ".format(
                                name_user))
                        elif i == 2:
                            print("atom : คุณ{} คิดว่าบริการทางการเงินด้านบัตรเครดิตของเราเป็นอย่างไร ?".format(
                                name_user))
                        elif i == 3:
                            print("atom : คุณ{} คิดว่าบริการโอนเงินระหว่างประเทศของเราเป็นอย่างไร ?".format(
                                name_user))
                        elif i == 4:
                            print("atom : คุณ{} คิดว่าบริการชำระค่าสินค้าและบริการของเราเป็นอย่างไร ?".format(
                                name_user))
                        elif i == 5:
                            print("atom : คุณ{} คิดว่าอัตราดอกเบี้ยค่าบริการบัตรเครดิตเป็นอย่างไร ?".format(
                                name_user))
                        text1 = input(">")
                        if i == 5:
                            exit_loop = True
                            humen += 1
                            print(
                                "atom : ขอบคุณ คุณ{}ที่สละเวลาครับ".format(name_user))
                            continue
                        if text1 in smile_verygood:
                            print("atom :", random.choice(smile_verygood_bot))
                            smile += 10
                            sum1 += 10
                        elif text1 in smile_good:
                            print("atom :", random.choice(smile_good_bot))
                            smile += 8
                            sum2 += 8
                        elif text1 in smile_well:
                            print("atom :", random.choice(smile_well_bot))
                            smile += 6
                            sum3 += 6
                        elif text1 in smile_bad:
                            print("atom :", random.choice(smile_bad_bot))
                            smile += 4
                            sum4 += 4
                        else:
                            print(
                                "atom : กรุณาตอบ \"ดีมากที่สุด\" \"ดีมาก\" \"ปานกลาง\" \"น้อย\'' ")
                            i -= 1
                elif text in no:
                    print("atom :", random.choice(nobot))
                else:
                    print("I don't understand..")
                if exit_loop == True:
                    break
########################################
    elif start == 2:
        start_admin()
########################################
    elif start == 3:
        print("\tกรุณาใส่รหัสผ่าน")
        user_admin = input("User : ")
        pass_admin = int(input("Pass : "))
        if user_admin == 'admin' and pass_admin == 123456789:
            sum1 = 0
            sum2 = 0
            sum3 = 0
            sum4 = 0
            smile = 0
            humen = 0
            print("----------------------------------------------------------")
            print("รีเซ็ตคะแนนเรียบร้อย")
            print("----------------------------------------------------------")
        else:
            print("*****************************************")
            print("รหัสผ่านผิด")
            print("*****************************************")
            continue
    ########################################
    elif start == 4:
        break
    else:
        print("----------------------------------------------------------")
        print("เลือกคำสั่ง 1 - 4")
        print("----------------------------------------------------------")
