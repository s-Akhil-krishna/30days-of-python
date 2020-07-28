
msg_template = """Hello {name},Welcome to {website}
Thanks for joining us..We are very happy to have you.
"""

def format_msg(my_name="Akhil",my_website="BingeCode"):
    formatted_msg =  msg_template.format(name=my_name,website=my_website)
    return formatted_msg