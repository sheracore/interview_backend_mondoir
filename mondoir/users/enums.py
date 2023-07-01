import enum


class Email(enum.Enum):
    SUBJECT = 'SUBJECT'
    BODY = 'MESSAGE'

    @property
    def get_value(self) -> str:
        if self.name == self.SUBJECT.name:
            return "SHERACORE from mondoir"
        if self.name == self.BODY.name:
            return "This is from mondoir, wellcome to mondoir, you can choose and get your apartment 100 online"
