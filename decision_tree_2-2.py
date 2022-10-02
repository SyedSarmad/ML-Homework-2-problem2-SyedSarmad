#-------------------------------------------------------------------------
# AUTHOR: Syed Sarmad
# FILENAME: decision_tree_2-2.py
# SPECIFICATION: Decsion tree with training and testing data 
# FOR: CS 4210- Assignment #2
# TIME SPENT: 11:44am-2:03pm
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    # so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]

    #transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]

    #--> add your Python code here

    #age-> Young = 1, Prepresbyopic = 2, Presbyopic = 3
    #Spectacle Prescription -> Myope = 1, Hypermetrope = 2 
    #Astigmatism -> yes = 1, no = 2
    #Tear Production Rate => normal = 1, reduced = 2


   
    #################################
    #print("TESTING START....")
    #################################

    temp = []
    for val in dbTraining: 
        temp = []

        #################################
        #print("VAL INSTANCE START")
        #print(val)
        #print("VAL INSTANCE END")
        #################################


        for val2_index in range(0, len(val)):
            if val2_index == (len(val) - 1) : 
                if val[val2_index] == 'Yes':
                    Y.append(1)
                elif val[val2_index] == 'No':
                    Y.append(2)
                
            else:
                if val[val2_index] == 'Young':
                    temp.append(1)
                elif val[val2_index] == 'Prepresbyopic':
                    temp.append(2)
                elif val[val2_index] == 'Presbyopic':
                    temp.append(3)
                elif val[val2_index] == 'Myope':
                    temp.append(1)
                elif val[val2_index] == 'Hypermetrope':
                    temp.append(2)
                elif val[val2_index] == 'Yes':
                    temp.append(1)
                elif val[val2_index] == 'No':
                    temp.append(2)
                elif val[val2_index] == 'Normal':
                    temp.append(1)
                elif val[val2_index] == 'Reduced':
                    temp.append(2)
            
        #################################
        #print("TEMP INSTANCE START")
        #print(temp)
        #print("TEMP INSTANCE END")
        #################################

        X.append(temp)
                
    #################################
    #print("PRINTING X START")
    #print(X)
    #print("PRINTING X END")

    #print("PRINTING Y START")
    #print(Y)
    #print("PRINTING Y END")

    #print("TESTING END....")
    #################################




    correct = 0
    count = 0
    accuracy_array = []
    lowest_accuracy = []

    #loop your training and test tasks 10 times here
    for i in range (10):

        #fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
        clf = clf.fit(X, Y)

        #read the test data and add this data to dbTest
        #--> add your Python code here
        #reading the training data in a csv file
        test_data = 'contact_lens_test.csv'
        dbTest = []
        with open(test_data, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i > 0: #skipping the header
                    dbTest.append (row)
        
        #print("PRINTING TEST DATA")
        #print(dbTest)

  
            
        dbTest_with_numbers = []

        for data in dbTest:
        
            #transform the features of the test instances to numbers following the same strategy done during training,
            #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
            #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
            #--> add your Python code here

            temp = []
            for val in data:
                if val == 'Young':
                    temp.append(1)
                elif val == 'Prepresbyopic':
                    temp.append(2)
                elif val == 'Presbyopic':
                    temp.append(3)
                elif val == 'Myope':
                    temp.append(1)
                elif val == 'Hypermetrope':
                    temp.append(2)
                elif val == 'Yes':
                    temp.append(1)
                elif val == 'No':
                    temp.append(2)
                elif val == 'Normal':
                    temp.append(1)
                elif val == 'Reduced':
                    temp.append(2)
            dbTest_with_numbers = temp

            #print("GREEN LANTERN")
            #print(dbTest_with_numbers[0:4])
            class_predicted = clf.predict([dbTest_with_numbers[0:4]])[0]
            

            

            #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
            #--> add your Python code here
            if class_predicted == dbTest_with_numbers[4]:
                correct += 1 
            count += 1
        
        accuracy = correct/count
        accuracy_array.append(accuracy)

        

        #find the lowest accuracy of this model during the 10 runs (training and test set)
        #--> add your Python code here

    lowest_accuracy.append(min(accuracy_array))

    #print the lowest accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here

    #print('final accuracy when training on contact_lens_training_1.csv')

    print(lowest_accuracy)


