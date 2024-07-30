from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,SubmitField,DateTimeField,IntegerField
from wtforms.validators import DataRequired
from datetime import datetime

class AddForm(FlaskForm):
    submit = SubmitField("Insert")

class InsertForm(FlaskForm):

    first_name = StringField("FIRST NAME :",validators=[DataRequired()])
    last_name = StringField("LAST NAME :",validators=[DataRequired()])
    std_class  = SelectField("CLASS :",validators=[DataRequired()],choices=[('first','first'),('second','second'),
                                                                          ('third','third'),('fourth','fourth'),
                                                                          ('fifth','fifth'),('sixth','sixth'),
                                              ('seventh','seventh'),('eighth','eighth'),('ninth','ninth'),
                                              ('tenth','tenth')])
    date = DateTimeField("DATE-TIME :",default=datetime.now())
    submit = SubmitField("NEW STUDENT")

class Delete_form(FlaskForm):
    submit = SubmitField("CONFIRM")


class UpdateForm(FlaskForm):

    id = IntegerField("ID :",validators=[DataRequired()])
    first_name = StringField("FIRST NAME :",validators=[DataRequired()])
    last_name = StringField("LAST NAME :",validators=[DataRequired()])
    std_class  = SelectField("CLASS :",validators=[DataRequired()],choices=[('first','first'),('second','second'),
                                                                          ('third','third'),('fourth','fourth'),
                                                                          ('fifth','fifth'),('sixth','sixth'),
                                              ('seventh','seventh'),('eighth','eighth'),('ninth','ninth'),
                                              ('tenth','tenth')])
    date = DateTimeField("DATE-TIME :",default=datetime.now())
    submit = SubmitField("UPDATE")
