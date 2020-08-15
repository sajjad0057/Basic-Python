'''
for know more about exception handling see
documentation Or W3school(Exception_handling)
**syntax:
      "try:
          probable error statement
      except error_type:
         message_statement....
      except error_type:
         message_statement....
         .
         .
      finaly:
        exact/right statement....
      "
'''
try:
    list = [20, 0, 30]
    result = list[0] / list[3]
    print(result,"done")
except ZeroDivisionError:
    print("Dividing by zero is not possible")
except IndexError:
    print("Index Error")
finally:
    print("successful")

