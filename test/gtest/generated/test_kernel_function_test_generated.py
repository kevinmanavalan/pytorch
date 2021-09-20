import torch
from torch.testing._internal.common_utils import TestCase, run_tests, run_cpp_test

TEST_BINARY = "build/bin/kernel_function_test"


class TestOperatorRegistrationTest_FunctionBasedKernel(TestCase):
    cpp_name = "OperatorRegistrationTest_FunctionBasedKernel"

    def test_givenKernel_whenRegistered_thenCanBeCalled(self):
        run_cpp_test(
            TEST_BINARY, self.cpp_name, "givenKernel_whenRegistered_thenCanBeCalled"
        )

    def test_givenKernel_whenRegisteredWithTorchLibraryAndTorchFn_thenCanBeCalled(self):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenKernel_whenRegisteredWithTorchLibraryAndTorchFn_thenCanBeCalled",
        )

    def test_givenCatchAllKernel_whenRegisteredWithTorchLibraryAndTorchFn_thenCanBeCalled(
        self,
    ):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenCatchAllKernel_whenRegisteredWithTorchLibraryAndTorchFn_thenCanBeCalled",
        )

    def test_givenMultipleOperatorsAndKernels_whenRegisteredInOneRegistrar_thenCallsRightKernel(
        self,
    ):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenMultipleOperatorsAndKernels_whenRegisteredInOneRegistrar_thenCallsRightKernel",
        )

    def test_givenMultipleOperatorsAndKernels_whenRegisteredInMultipleRegistrars_thenCallsRightKernel(
        self,
    ):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenMultipleOperatorsAndKernels_whenRegisteredInMultipleRegistrars_thenCallsRightKernel",
        )

    def test_givenKernelWithoutOutput_whenRegistered_thenCanBeCalled(self):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenKernelWithoutOutput_whenRegistered_thenCanBeCalled",
        )

    def test_givenKernelWithZeroOutputs_whenRegistered_thenCanBeCalled(self):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenKernelWithZeroOutputs_whenRegistered_thenCanBeCalled",
        )

    def test_givenKernelWithIntOutput_whenRegistered_thenCanBeCalled(self):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenKernelWithIntOutput_whenRegistered_thenCanBeCalled",
        )

    def test_givenKernelWithTensorOutput_whenRegistered_thenCanBeCalled(self):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenKernelWithTensorOutput_whenRegistered_thenCanBeCalled",
        )

    def test_givenKernelWithTensorListOutput_whenRegistered_thenCanBeCalled(self):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenKernelWithTensorListOutput_whenRegistered_thenCanBeCalled",
        )

    def test_givenKernelWithIntListOutput_whenRegistered_thenCanBeCalled(self):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenKernelWithIntListOutput_whenRegistered_thenCanBeCalled",
        )

    def test_givenKernelWithMultipleOutputs_whenRegistered_thenCanBeCalled(self):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenKernelWithMultipleOutputs_whenRegistered_thenCanBeCalled",
        )

    def test_givenKernelWithTensorInputByReference_withOutput_whenRegistered_thenCanBeCalled(
        self,
    ):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenKernelWithTensorInputByReference_withOutput_whenRegistered_thenCanBeCalled",
        )

    def test_givenKernelWithTensorInputByValue_withOutput_whenRegistered_thenCanBeCalled(
        self,
    ):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenKernelWithTensorInputByValue_withOutput_whenRegistered_thenCanBeCalled",
        )

    def test_givenKernelWithTensorInputByReference_withoutOutput_whenRegistered_thenCanBeCalled(
        self,
    ):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenKernelWithTensorInputByReference_withoutOutput_whenRegistered_thenCanBeCalled",
        )

    def test_givenKernelWithTensorInputByValue_withoutOutput_whenRegistered_thenCanBeCalled(
        self,
    ):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenKernelWithTensorInputByValue_withoutOutput_whenRegistered_thenCanBeCalled",
        )

    def test_givenKernelWithIntInput_withoutOutput_whenRegistered_thenCanBeCalled(self):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenKernelWithIntInput_withoutOutput_whenRegistered_thenCanBeCalled",
        )

    def test_givenKernelWithIntInput_withOutput_whenRegistered_thenCanBeCalled(self):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenKernelWithIntInput_withOutput_whenRegistered_thenCanBeCalled",
        )

    def test_givenKernelWithIntListInput_withoutOutput_whenRegistered_thenCanBeCalled(
        self,
    ):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenKernelWithIntListInput_withoutOutput_whenRegistered_thenCanBeCalled",
        )

    def test_givenKernelWithIntListInput_withOutput_whenRegistered_thenCanBeCalled(
        self,
    ):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenKernelWithIntListInput_withOutput_whenRegistered_thenCanBeCalled",
        )

    def test_givenKernelWithTensorListInput_withoutOutput_whenRegistered_thenCanBeCalled(
        self,
    ):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenKernelWithTensorListInput_withoutOutput_whenRegistered_thenCanBeCalled",
        )

    def test_givenKernelWithTensorListInput_withOutput_whenRegistered_thenCanBeCalled(
        self,
    ):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenKernelWithTensorListInput_withOutput_whenRegistered_thenCanBeCalled",
        )

    def test_givenKernelWithDictInput_withoutOutput_whenRegistered_thenCanBeCalled(
        self,
    ):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenKernelWithDictInput_withoutOutput_whenRegistered_thenCanBeCalled",
        )

    def test_givenKernelWithDictInput_withOutput_whenRegistered_thenCanBeCalled(self):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenKernelWithDictInput_withOutput_whenRegistered_thenCanBeCalled",
        )

    def test_givenKernelWithDictOutput_whenRegistered_thenCanBeCalled(self):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenKernelWithDictOutput_whenRegistered_thenCanBeCalled",
        )

    def test_givenFallbackKernelWithoutAnyArguments_whenRegistered_thenCanBeCalled(
        self,
    ):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenFallbackKernelWithoutAnyArguments_whenRegistered_thenCanBeCalled",
        )

    def test_givenFallbackKernelWithoutTensorArguments_whenRegistered_thenCanBeCalled(
        self,
    ):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenFallbackKernelWithoutTensorArguments_whenRegistered_thenCanBeCalled",
        )

    def test_givenKernelWithOptionalInputs_withoutOutput_whenRegistered_thenCanBeCalled(
        self,
    ):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenKernelWithOptionalInputs_withoutOutput_whenRegistered_thenCanBeCalled",
        )

    def test_givenKernelWithOptionalInputs_withOutput_whenRegistered_thenCanBeCalled(
        self,
    ):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenKernelWithOptionalInputs_withOutput_whenRegistered_thenCanBeCalled",
        )

    def test_givenKernelWithOptionalInputs_withMultipleOutputs_whenRegistered_thenCanBeCalled(
        self,
    ):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenKernelWithOptionalInputs_withMultipleOutputs_whenRegistered_thenCanBeCalled",
        )

    def test_givenKernel_whenRegistered_thenCanBeCalledUnboxed(self):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenKernel_whenRegistered_thenCanBeCalledUnboxed",
        )

    def test_givenKernel_whenRegisteredWithoutSpecifyingSchema_thenInfersSchema(self):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenKernel_whenRegisteredWithoutSpecifyingSchema_thenInfersSchema",
        )

    def test_givenMismatchedKernel_withDifferentNumArguments_whenRegistering_thenFails(
        self,
    ):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenMismatchedKernel_withDifferentNumArguments_whenRegistering_thenFails",
        )

    def test_givenMismatchedKernel_withDifferentArgumentType_whenRegistering_thenFails(
        self,
    ):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenMismatchedKernel_withDifferentArgumentType_whenRegistering_thenFails",
        )

    def test_givenMismatchedKernel_withDifferentNumReturns_whenRegistering_thenFails(
        self,
    ):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenMismatchedKernel_withDifferentNumReturns_whenRegistering_thenFails",
        )

    def test_givenMismatchedKernel_withDifferentReturnTypes_whenRegistering_thenFails(
        self,
    ):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenMismatchedKernel_withDifferentReturnTypes_whenRegistering_thenFails",
        )


class TestNewOperatorRegistrationTest_FunctionBasedKernel(TestCase):
    cpp_name = "NewOperatorRegistrationTest_FunctionBasedKernel"

    def test_givenKernel_whenRegistrationRunsOutOfScope_thenCannotBeCalledAnymore(self):
        run_cpp_test(
            TEST_BINARY,
            self.cpp_name,
            "givenKernel_whenRegistrationRunsOutOfScope_thenCannotBeCalledAnymore",
        )


if __name__ == "__main__":
    run_tests()
