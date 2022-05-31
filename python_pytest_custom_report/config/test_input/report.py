import xml.etree.ElementTree as ET


def parse_xml(xmlfile):

    tree = ET.parse(xmlfile)

    root = tree.getroot()

    tests = []

    for testsuites_element in root:
        for testsuite_element in testsuites_element:

            test = {"name": testsuite_element.attrib['name'], "result": True}

            for child in testsuite_element:
                if child.tag == "failure":
                    test["result"] = False

            tests.append(test)

    return tests

def test_result(tests):
    test_num = 0
    for test in tests:
        test_num += 1
        if test["result"] == True:
            print(str(test_num) + ". PASS   " + test["name"])
        else:
            print(str(test_num) + ". FAIL   " + test["name"])

def main():
    print("Tests")
    tests = parse_xml('good.xml')
    test_result(tests)
    tests = parse_xml('bad.xml')
    test_result(tests)


if __name__ == "__main__":

    main()
