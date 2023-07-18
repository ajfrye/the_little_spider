class Character:
    def __init__(self, path_to_image):
        self.path_to_image = path_to_image
        self.front_left_hand = None
        self.front_right_hand = None
        self.rear_left_hand = None
        self.rear_right_hand = None
        self.armor = None
        self.accessory = None
        self.health = 25
        self.max_health = 25

    def equip_hand(self, hand_number,equipment):
        self.front_left_hand = equipment

    def equip_front_right_hand(self, equipment):
        self.front_right_hand = equipment

    def equip_rear_left_hand(self, equipment):
        self.rear_left_hand = equipment

    def equip_rear_right_hand(self, equipment):
        self.rear_right_hand = equipment

    def equip_armor(self, equipment):
        self.armor = equipment

    def equip_accessory(self, equipment):
        self.accessory = equipment

    def update_health(self, delta_health):
        health = self.health + delta_health
        if (health > self.max_health):
            self.health = self.max_health
        else:
            self.health = health

    def update_max_health(self, delta_health):
        self.max_health += delta_health