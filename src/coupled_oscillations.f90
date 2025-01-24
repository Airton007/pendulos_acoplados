module coupled_oscillations
  implicit none
  private

  public :: say_hello
contains
  subroutine say_hello
    print *, "Hello, coupled_oscillations!"
  end subroutine say_hello
end module coupled_oscillations
