from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


class AnonMembershipExistenceThrottle(AnonRateThrottle):
    scope = 'check_membership_existence_anon'


class AnonOtpThrottle(AnonRateThrottle):
    scope = 'anon_otp'


class UserOtpThrottle(UserRateThrottle):
    scope = 'user_otp'
