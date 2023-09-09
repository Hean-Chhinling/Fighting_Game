import pygame


class Fighter():
    def __init__(self, player, x, y, flip, data, sprite_sheet, animation_steps, sound):
        self.player = player
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.flip = flip
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.action = 0  # 0 ide, 1  run, 2 attack_type2, 3 was hit, 4 jump, 5 attack_type1
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.rect = pygame.Rect((x, y, 90, 180))
        self.vel_y = 0
        self.running = False
        self.jump = False
        self.attack_type = 0
        self.attack_cooldown = 0
        self.attacking = False
        self.attack_sound = sound
        self.hit = False
        self.health = 100
        self.alive = True

    # Load Images for sprite sheets
    def load_images(self, sprite_sheet, animation_steps):
        # extract images from spritesheet
        animation_list = []
        for y, animation in enumerate(animation_steps):
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(x * self.size, y * self.size, self.size, self.size)
                temp_img_list.append(
                    pygame.transform.scale(temp_img, (self.size * self.image_scale, self.size * self.image_scale)))
            animation_list.append(temp_img_list)
            print(animation_list)
        return animation_list

    # Function for movement
    def move(self, screen_width, screen_height, surface, target, round_over):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0
        self.running = False
        self.attack_type = 0

        key = pygame.key.get_pressed()

        # Can only perform one action at a time
        if self.attacking == False and self.alive == True and round_over == False:
            # Check player1 control
            if self.player == 1:
                if key[pygame.K_a]:
                    dx = -SPEED
                    self.running = True
                if key[pygame.K_d]:
                    dx = SPEED
                    self.running = True
                if key[pygame.K_w] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True
                # Attack Key
                if key[pygame.K_q] or key[pygame.K_e]:
                    self.attack(surface, target)
                    # Determine which attack type
                    if key[pygame.K_q]:
                        self.attack_type = 1
                    if key[pygame.K_e]:
                        self.attack_type = 2

            # Check player2 control
            if self.player == 2:
                if key[pygame.K_LEFT]:
                    dx = -SPEED
                    self.running = True
                if key[pygame.K_RIGHT]:
                    dx = SPEED
                    self.running = True
                if key[pygame.K_UP] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True
                # Attack Key
                if key[pygame.K_p] or key[pygame.K_l]:
                    self.attack(surface, target)
                    # Determine which attack type
                    if key[pygame.K_p]:
                        self.attack_type = 1
                    if key[pygame.K_l]:
                        self.attack_type = 2


        # apply gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

        # ensure player doesn't go out of the screen

        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 70:
            self.vel_y = 0
            dy = screen_height - 70 - self.rect.bottom
            self.jump = False

        # ensure players face each other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        # subtract attack cooldown
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        # Update player position
        self.rect.x += dx
        self.rect.y += dy

    # Update animation
    def update_animation(self):
        # check what action is performing
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.update_action(3)
        elif self.hit:
            self.update_action(4)
        elif self.attacking == True:
            if self.attack_type == 1:
                self.update_action(11)
            elif self.attack_type == 2:
                self.update_action(15)
        elif self.jump == True:
            self.update_action(2)
        elif self.running == True:
            self.update_action(1)
        else:
            self.update_action(0)

        animation_cooldown = 200
        self.image = self.animation_list[self.action][self.frame_index]
        # Check if time has passed for new update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        # Check if the frame index has finished to the end of the screen
        if self.frame_index >= len(self.animation_list[self.action]):
            # check if the player is dead then end the animation
            if self.alive == False:
                self.frame_index = len(self.animation_list[self.action]) - 1
                print(self.frame_index)
            else:
                self.frame_index = 0
                # check if an attack was executed
                if self.action == 11 or self.action == 15:
                    self.attacking = False
                    self.attack_cooldown = 10
                # check if damage was taken
                if self.action == 4:
                    self.hit = False
                    # check if the player is in the middle of attack
                    self.attacking = False
                    self.attack_cooldown = 10

    def attack(self, surface, target):
        if self.attack_cooldown == 0:
            # execute attack
            self.attacking = True
            self.attack_sound.play()
            attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
            if attacking_rect.colliderect(target.rect):
                target.health -= 10
                target.hit = True
            pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def update_action(self, new_action):
        # check to see if the new action different from the previous one
        if new_action != self.action:
            self.action = new_action
            # update the animatioin settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()


    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.flip, False)
        # pygame.draw.rect(surface, (255, 0, 0), self.rect)
        surface.blit(img, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))

