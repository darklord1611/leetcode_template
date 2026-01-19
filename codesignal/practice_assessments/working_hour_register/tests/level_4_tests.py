import inspect, os, sys
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from timeout_decorator import timeout
import unittest
from working_hour_register_impl import WorkingHourRegisterImpl


class Level4Tests(unittest.TestCase):
    """
    Level 4 tests for Working Hour Register - Shift Management and Advanced Analytics

    Tests cover: CREATE_SHIFT, ASSIGN_SHIFT, GET_SHIFT_COMPLIANCE, GENERATE_PAYROLL_REPORT,
                 GET_SHIFT_STATISTICS, FIND_UNCOVERED_SHIFTS, EXPORT_TIMESHEET,
                 CALCULATE_WEEKLY_OVERTIME
    All tests have a 0.4 second timeout.
    """

    failureException = Exception

    def setUp(self):
        """Create a fresh WorkingHourRegister instance for each test."""
        self.whr = WorkingHourRegisterImpl()

    @timeout(0.4)
    def test_level_4_case_01_create_shift(self):
        """Test creating a shift template."""
        result = self.whr.create_shift("morning1", "09:00", "17:00", "MORNING")
        self.assertEqual(result, "true")

    @timeout(0.4)
    def test_level_4_case_02_assign_shift(self):
        """Test assigning a shift to an employee."""
        self.whr.create_shift("morning1", "09:00", "17:00", "MORNING")
        result = self.whr.assign_shift("emp001", "2024-01-15", "morning1")
        self.assertEqual(result, "true")

    @timeout(0.4)
    def test_level_4_case_03_get_shift_compliance_compliant(self):
        """Test shift compliance when employee works expected hours."""
        # Create morning shift (8 hours), employee works 8 hours
        self.whr.create_shift("morning1", "09:00", "17:00", "MORNING")
        self.whr.clock_in(1705309200000, "emp001")  # 2024-01-15 09:00
        self.whr.clock_out(1705338000000, "emp001")  # 2024-01-15 17:00
        self.whr.assign_shift("emp001", "2024-01-15", "morning1")
        result = self.whr.get_shift_compliance("emp001", "2024-01-15")
        self.assertEqual(result, "compliant")

    @timeout(0.4)
    def test_level_4_case_04_get_shift_compliance_non_compliant(self):
        """Test shift compliance when employee doesn't work expected hours."""
        # Create morning shift (8 hours), employee works 6 hours
        self.whr.create_shift("morning1", "09:00", "17:00", "MORNING")
        self.whr.clock_in(1705309200000, "emp001")  # 2024-01-15 09:00
        self.whr.clock_out(1705330800000, "emp001")  # 2024-01-15 15:00 (6 hours)
        self.whr.assign_shift("emp001", "2024-01-15", "morning1")
        result = self.whr.get_shift_compliance("emp001", "2024-01-15")
        self.assertEqual(result, "non-compliant")

    @timeout(0.4)
    def test_level_4_case_05_generate_payroll_report(self):
        """Test generating payroll report for multiple employees."""
        # emp001 works 8 hours at $25/hr = $200
        self.whr.clock_in(1705309200000, "emp001")
        self.whr.clock_out(1705338000000, "emp001")
        self.whr.set_hourly_rate("emp001", 25)
        # emp002 works 8 hours at $20/hr = $160
        self.whr.clock_in(1705395600000, "emp002")
        self.whr.clock_out(1705424400000, "emp002")
        self.whr.set_hourly_rate("emp002", 20)
        result = self.whr.generate_payroll_report("2024-01-15", "2024-01-16")
        self.assertEqual(result, "emp001(200), emp002(160)")

    @timeout(0.4)
    def test_level_4_case_06_get_shift_statistics(self):
        """Test getting statistics for a shift type."""
        # Create morning shifts and assign to employees
        self.whr.create_shift("morning1", "09:00", "17:00", "MORNING")
        self.whr.clock_in(1705309200000, "emp001")  # 8 hours
        self.whr.clock_out(1705338000000, "emp001")
        self.whr.assign_shift("emp001", "2024-01-15", "morning1")
        self.whr.clock_in(1705395600000, "emp002")  # 8 hours
        self.whr.clock_out(1705424400000, "emp002")
        self.whr.assign_shift("emp002", "2024-01-16", "morning1")
        result = self.whr.get_shift_statistics("MORNING", "2024-01-15", "2024-01-16")
        self.assertEqual(result, "total_hours:16,employees:2,avg_hours:8")

    @timeout(0.4)
    def test_level_4_case_07_find_uncovered_shifts(self):
        """Test finding shifts that were assigned but not worked."""
        self.whr.create_shift("morning1", "09:00", "17:00", "MORNING")
        # Assign shift to emp003 but emp003 doesn't work
        self.whr.assign_shift("emp003", "2024-01-15", "morning1")
        result = self.whr.find_uncovered_shifts("2024-01-15")
        self.assertEqual(result, "emp003:morning1")

    @timeout(0.4)
    def test_level_4_case_08_export_timesheet(self):
        """Test exporting timesheet for an employee."""
        # emp001 works 8 hours on 2024-01-15
        self.whr.clock_in(1705309200000, "emp001")
        self.whr.clock_out(1705338000000, "emp001")
        result = self.whr.export_timesheet("emp001", "2024-01-15", "2024-01-16")
        self.assertEqual(result, "2024-01-15(8)")

    @timeout(0.4)
    def test_level_4_case_09_calculate_weekly_overtime(self):
        """Test calculating weekly overtime (hours > 40 in a week)."""
        # Employee works 44 hours in a week, overtime = 4
        self.whr.clock_in(1705309200000, "emp003")
        self.whr.clock_out(1705467600000, "emp003")  # 44 hours later
        result = self.whr.calculate_weekly_overtime("emp003", "2024-01-15")
        self.assertEqual(result, "4")

    @timeout(0.4)
    def test_level_4_case_10_complete_scenario(self):
        """Test complete scenario from test_data_4."""
        # Create shifts
        self.assertEqual(self.whr.create_shift("morning1", "09:00", "17:00", "MORNING"), "true")
        self.assertEqual(self.whr.create_shift("evening1", "13:00", "21:00", "EVENING"), "true")
        # emp001 works 2024-01-15
        self.assertEqual(self.whr.clock_in(1705309200000, "emp001"), "true")
        self.assertEqual(self.whr.clock_out(1705338000000, "emp001"), "8")
        self.assertEqual(self.whr.assign_shift("emp001", "2024-01-15", "morning1"), "true")
        self.assertEqual(self.whr.get_shift_compliance("emp001", "2024-01-15"), "compliant")
        # emp002 works 2024-01-16
        self.assertEqual(self.whr.clock_in(1705395600000, "emp002"), "true")
        self.assertEqual(self.whr.clock_out(1705424400000, "emp002"), "8")
        self.assertEqual(self.whr.assign_shift("emp002", "2024-01-16", "morning1"), "true")
        # Set rates and generate payroll
        self.assertEqual(self.whr.set_hourly_rate("emp001", 25), "true")
        self.assertEqual(self.whr.set_hourly_rate("emp002", 20), "true")
        self.assertEqual(self.whr.generate_payroll_report("2024-01-15", "2024-01-16"), "emp001(200), emp002(160)")
        self.assertEqual(self.whr.get_shift_statistics("MORNING", "2024-01-15", "2024-01-16"), "total_hours:16,employees:2,avg_hours:8")
        # Test uncovered shifts
        self.assertEqual(self.whr.assign_shift("emp003", "2024-01-15", "morning1"), "true")
        self.assertEqual(self.whr.find_uncovered_shifts("2024-01-15"), "emp003:morning1")
        # Export timesheet
        self.assertEqual(self.whr.export_timesheet("emp001", "2024-01-15", "2024-01-16"), "2024-01-15(8)")
        # Weekly overtime
        self.assertEqual(self.whr.clock_in(1705309200000, "emp003"), "true")
        self.assertEqual(self.whr.clock_out(1705467600000, "emp003"), "44")
        self.assertEqual(self.whr.calculate_weekly_overtime("emp003", "2024-01-15"), "4")


if __name__ == '__main__':
    unittest.main()
