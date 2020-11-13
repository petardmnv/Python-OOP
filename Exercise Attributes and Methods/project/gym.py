from typing import Dict, List

from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    customers: List[Customer]
    trainers: List[Trainer]
    equipment: List[Equipment]
    plans: List[ExercisePlan]
    subscriptions: List[Subscription]

    customers_id: Dict[int, Customer]
    trainers_id: Dict[int, Trainer]
    equipment_id: Dict[int, Equipment]
    plans_id: Dict[int, ExercisePlan]
    subscriptions_id: Dict[int, Subscription]

    def __init__(self):
        self.equipment = []
        self.customers = []
        self.trainers = []
        self.plans = []
        self.subscriptions = []

        self.customers_id = {}
        self.trainers_id = {}
        self.equipment_id = {}
        self.plans_id = {}
        self.subscriptions_id = {}

    def add_customer(self, customer: Customer):
        if customer in self.customers:
            return
        self.customers.append(customer)
        self.customers_id[customer.id] = customer

    def add_trainer(self, trainer: Trainer):
        if trainer in self.trainers:
            return
        self.trainers.append(trainer)
        self.trainers_id[trainer.id] = trainer

    def add_equipment(self, equipment: Equipment):
        if equipment in self.equipment:
            return
        self.equipment.append(equipment)
        self.equipment_id[equipment.id] = equipment

    def add_plan(self, plan: ExercisePlan):
        if plan in self.plans:
            return
        self.plans.append(plan)
        self.plans_id[plan.id] = plan

    def add_subscription(self, subscription: Subscription):
        if subscription in self.subscriptions:
            return
        self.subscriptions.append(subscription)
        self.subscriptions_id[subscription.id] = subscription

    def subscription_info(self, subscription_id: int):
        curr_s = self.subscriptions_id[subscription_id]
        customer = self.customers_id[curr_s.customer_id]
        trainer = self.trainers_id[curr_s.trainer_id]
        plan = self.plans_id[curr_s.exercise_id]
        equipment = self.equipment_id[plan.equipment_id]

        return '\n'.join(map(str, [curr_s, customer, trainer, equipment, plan]))


